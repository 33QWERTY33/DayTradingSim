from yfinance.base import TickerBase
from yfinance.exceptions import YFinanceException
from django.shortcuts import render, redirect

# Create your views here.

def get_ticker(request):
    return render(request, "get-ticker.html")

def incorrect_ticker(request):
    return render(request, "incorrect-ticker.html")

def display_ticker_info(request):
    ticker_obj = TickerBase(request.POST["ticker"])
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

    return render(request, "display-ticker-info.html", {"data": current_info, "news": news})