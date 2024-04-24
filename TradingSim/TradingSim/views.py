from yfinance.base import TickerBase
from django.shortcuts import render

def get_ticker(request):
    return render(request, "get-ticker.html")

def display_ticker_info(request):
    try:
        ticker_obj = TickerBase(request.POST["ticker"])
        current_info = ticker_obj.get_info()
        current_price = current_info["currentPrice"]
        if current_price == None: raise KeyError
        full_name = "PLACEHOLDER"
        full_name = current_info["longName"]
        if full_name == None: raise KeyError
    except KeyError:
        print("ERROR OCCURRED")
        print(current_info.keys())
        current_price = current_info["previousClose"]
        full_name = current_info["longName"]

    return render(request, "display-ticker-info.html", {"current_price":current_price, "full_name":full_name})