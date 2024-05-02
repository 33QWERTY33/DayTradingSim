from yfinance.base import TickerBase
from yfinance.exceptions import YFinanceException
from django.shortcuts import render, redirect
from django.http import HttpResponse
import matplotlib.pyplot as plt
import os
# Create your views here.

def get_ticker(request):
    return render(request, "get-ticker.html")

def incorrect_ticker(request):
    return render(request, "incorrect-ticker.html")

def display_ticker_info(request):
    if request.method == "POST":
        ticker_obj = TickerBase(request.POST.get("ticker"))
        # store ticker object

        keys_used = ["currentPrice", "symbol", "longName", "averageVolume10days", "quoteType", "dayHigh", "dayLow", "regularMarketOpen", "regularMarketPreviousClose"]
        # list of keys used in webpage to set default vals

        try:
            current_info = ticker_obj.get_info()
        except YFinanceException:
            return redirect("ticker:incorrect-ticker")
        # handling incorrect ticker input

        current_info = ticker_obj.get_info()

        try:
            current_info["currentPrice"]
        except KeyError:
            current_info["currentPrice"] = current_info["navPrice"]
        # stocks current price is stored in currentPrice key, ETF current price is stored in navPrice
        
        for key in keys_used:
            try:
                current_info[key]
            except KeyError:
                current_info[key] = "Not found"
        # set default values for all data not included

        news = ticker_obj.get_news()
        # list of news articles

        price_history = ticker_obj.history("2y")["Open"]

        plt.style.use('dark_background')

        plt.figure(figsize=(20,10))

        plt.plot(price_history)

        plt.title(request.POST.get("ticker").upper() + " 2 Year Price Report")

        plt.xlabel("Date")
        plt.ylabel("Price")

        plt.axhline(price_history.mean(), color="yellow", linestyle="--")

        plt.savefig(os.path.join("static", "assets", "tickerReports", "2YearReport.png"))

        return render(request, "display-ticker-info.html", {"data": current_info, "news": news})
    else:
        return HttpResponse()
    # there is a situation with the request object not having a POST attribute to access causing some internal django errors.
    # This fix is not ideal, but it's a patch for now