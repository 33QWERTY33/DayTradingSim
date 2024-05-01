from django.shortcuts import render, redirect
from .models import BuyOrders, SellOrders
from yfinance.base import TickerBase
from datetime import datetime
from UsersApp.models import UserPortfolio

# Create your views here.
def place_buy_order(request):
    user_portfolio = UserPortfolio.objects.get(username=request.user)
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
            new_buy_order.buyPrice = buyprice
            new_buy_order.stockAmount = stockAmount
            new_buy_order.cashAmount = cashAmount
            new_buy_order.sellTrigger = sellTrigger
            new_buy_order.pending = pending
            new_buy_order.buyDate = buydate

            user_portfolio.investedAmount += cashAmount
            user_portfolio.liquidAmount = user_portfolio.totalPortfolioAmount - user_portfolio.investedAmount

            user_portfolio.save()
            new_buy_order.save()
        except:
            return redirect("ticker:incorrect-ticker")

        return redirect("home")
    return render(request, "place-buy-order.html", {"portfolio": user_portfolio})
    

def place_sell_order(request):
    user_portfolio = UserPortfolio.objects.get(username=request.user)
    if request.method == "POST":
        id = request.POST.get('id')
        try:
            buy_order = BuyOrders.objects.get(id=id)
            sell_order = SellOrders()
            sell_order.id = buy_order.id
            sell_order.user = buy_order.user
            sell_order.ticker = buy_order.ticker
            sell_order.buyPrice = buy_order.buyPrice
            sell_order.cashAmount = buy_order.cashAmount
            sell_order.stockAmount = buy_order.stockAmount
            sell_order.sellPrice = float(TickerBase(sell_order.ticker).get_info().get("currentPrice") or TickerBase(sell_order.ticker).get_info().get("navPrice"))
            sell_order.profit = (buy_order.stockAmount * sell_order.sellPrice )- buy_order.cashAmount
            sell_order.buyDate = buy_order.buyDate
            sell_order.sellDate = datetime.now().date()

            user_portfolio.totalPortfolioAmount += sell_order.profit
            user_portfolio.investedAmount -= sell_order.cashAmount
            user_portfolio.liquidAmount = user_portfolio.totalPortfolioAmount - user_portfolio.investedAmount

            buy_order.delete()
            user_portfolio.save()
            sell_order.save()
        except:
            return redirect("ticker:incorrect-ticker")
        return redirect("home")

    currentOrders = BuyOrders.objects.filter(user=request.user).order_by("-buyDate")

    return render(request, "place-sell-order.html", {"currentOrders": currentOrders, "portfolio":user_portfolio})

def sell_order_details(request, id):
    order = SellOrders.objects.get(id=id)

    return render(request, "sell-order-details.html", {"order": order})

def buy_order_details(request, id):

    order = BuyOrders.objects.get(id=id)

    return render(request, "buy-order-details.html", {"order": order})
