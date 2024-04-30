from django.shortcuts import render
from .models import BuyOrders
from yfinance.base import TickerBase
from datetime import datetime

# Create your views here.
def place_buy_order(request):
    if request.method == "POST":
        new_buy_order = BuyOrders()

        user = request.POST.get("username")
        ticker = request.POST.get("ticker").upper()
        buyprice = float(TickerBase(ticker).get_info().get("currentPrice") or TickerBase(ticker).get_info().get("navPrice"))
        stockAmount = float(request.POST.get("stockAmount"))
        cashAmount = buyprice * stockAmount
        sellTrigger = float(request.POST.get("sellTrigger"))
        pending = True
        buydate = datetime.now().date()

        new_buy_order.user = user
        new_buy_order.ticker = ticker
        new_buy_order.buyprice = buyprice
        new_buy_order.stockAmount = stockAmount
        new_buy_order.cashAmount = cashAmount
        new_buy_order.sellTrigger = sellTrigger
        new_buy_order.pending = pending
        new_buy_order.buydate = buydate

        new_buy_order.save()

    return render(request, "place-buy-order.html")

def place_sell_order(request):
    currentOrders = BuyOrders.objects.filter(user=request.user).order_by("-buydate")

    return render(request, "place-sell-order.html", {"currentOrders": currentOrders})

def order_details(request, id):

    order = BuyOrders.objects.get(id=id)

    return render(request, "order-details.html", {"order": order})