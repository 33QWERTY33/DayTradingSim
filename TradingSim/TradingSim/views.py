from yfinance.base import TickerBase
from django.shortcuts import render

def get_ticker(request):
    return render(request, "get-ticker.html")

def incorrect_ticker(request):
    return render(request, "incorrect-ticker.html")

def display_ticker_info(request):
    ticker_obj = TickerBase(request.POST["ticker"])

    keys_used = ["currentPrice", "symbol", "longName", "averageVolume10days", "quoteType", "dayHigh", "dayLow", "regularMarketOpen", "regularMarketPreviousClose"]

    current_info = ticker_obj.get_info()
    if len(current_info) < 3: 
        return render(request, "incorrect-ticker.html")
    
    try:
        current_info["currentPrice"]
    except KeyError:
        current_info["currentPrice"] = current_info["navPrice"]
    
    for key in keys_used:
        try:
           current_info[key]
        except KeyError:
            current_info[key] = "Not found"

    news = ticker_obj.get_news()

    return render(request, "display-ticker-info.html", {"data": current_info, "news": news})