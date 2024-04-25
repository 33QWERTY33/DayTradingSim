from yfinance.base import TickerBase
from django.shortcuts import render

def log_in(request):
    return render(request, "log-in.html")

def home(request):
    # gather user information to display to page
    return render(request, "home.html", {"PLACEHOLDER": "PLACEHOLDER"})

def get_ticker(request):
    return render(request, "get-ticker.html")

def incorrect_ticker(request):
    return render(request, "incorrect-ticker.html")

def display_ticker_info(request):
    ticker_obj = TickerBase(request.POST["ticker"])
    # store ticker object

    keys_used = ["currentPrice", "symbol", "longName", "averageVolume10days", "quoteType", "dayHigh", "dayLow", "regularMarketOpen", "regularMarketPreviousClose"]
    # list of keys used in webpage to set default vals

    current_info = ticker_obj.get_info()
    # core information
    if len(current_info) < 3: 
        # bad request dict response has very few key:vals
        return render(request, "incorrect-ticker.html")
    
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