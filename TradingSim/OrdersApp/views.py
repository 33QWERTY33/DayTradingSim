from django.shortcuts import render, redirect
from .models import BuyOrders, SellOrders
from yfinance.base import TickerBase
from datetime import datetime

# Create your views here.
def place_buy_order(request):
    if request.method == "POST":
        try:
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
        except:
            return redirect("ticker:incorrect-ticker")

        return redirect("home")
    return render(request, "place-buy-order.html")
    

def place_sell_order(request):
    if request.method == "POST":
        id = request.POST.get('id')
        try:
            buy_order = BuyOrders.objects.get(id=id)

            sell_order = SellOrders()
            sell_order.user = buy_order.user
            sell_order.ticker = buy_order.ticker
            sell_order.buyprice = buy_order.buyprice
            sell_order.cashAmount = buy_order.cashAmount
            sell_order.stockAmount = buy_order.stockAmount
            sell_order.sellPrice = float(TickerBase(sell_order.ticker).get_info().get("currentPrice") or TickerBase(sell_order.ticker).get_info().get("navPrice"))
            sell_order.profit = (buy_order.stockAmount * sell_order.sellPrice )- buy_order.cashAmount
            sell_order.buydate = buy_order.buydate
            sell_order.sellDate = datetime.now().date()

            buy_order.delete()
            sell_order.save()
        except:
            return redirect("ticker:incorrect-ticker")

    currentOrders = BuyOrders.objects.filter(user=request.user).order_by("-buydate")

    return render(request, "place-sell-order.html", {"currentOrders": currentOrders})

def order_details(request, id):

    order = BuyOrders.objects.get(id=id)

    return render(request, "order-details.html", {"order": order})