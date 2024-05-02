from django.shortcuts import render, redirect
from .models import BuyOrders, SellOrders
from yfinance.base import TickerBase
from datetime import datetime
from UsersApp.models import UserPortfolio
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
@login_required(login_url="/user/login")
def place_buy_order(request):
    user_portfolio = UserPortfolio.objects.get(username=request.user)
    if request.method == "POST":
        try:
            hour = datetime.now().hour

            new_buy_order = BuyOrders()

            new_buy_order.user = request.POST.get("username")
            new_buy_order.ticker = request.POST.get("ticker").upper()
            new_buy_order.buyPrice = float(TickerBase(new_buy_order.ticker).get_info().get("currentPrice") or TickerBase(new_buy_order.ticker).get_info().get("navPrice"))
            new_buy_order.stockAmount = float(request.POST.get("stockAmount"))
            new_buy_order.cashAmount = new_buy_order.buyPrice * new_buy_order.stockAmount
            new_buy_order.buyDate = datetime.now().date()


            # setting BuyOrders necessary fields

            if new_buy_order.cashAmount > user_portfolio.liquidAmount:
                return redirect("order:insufficient-funds")
            # broke people land

            # #####################################  REMOVE FOR PRESENTATION/TESTING #####################################
            if hour < 9 or hour > 16:
                return redirect("order:outside-market-hours")
            # #####################################  REMOVE FOR PRESENTATION/TESTING #####################################

            user_portfolio.investedAmount += new_buy_order.cashAmount
            user_portfolio.liquidAmount = user_portfolio.totalPortfolioAmount - user_portfolio.investedAmount
            # updating UserPortfolio fields

            user_portfolio.save()
            new_buy_order.save()
        except ZeroDivisionError:
            return redirect("ticker:incorrect-ticker")

        return redirect("home")
    return render(request, "place-buy-order.html", {"portfolio": user_portfolio})
    
@login_required(login_url="/user/login")
def place_sell_order(request):
    user_portfolio = UserPortfolio.objects.get(username=request.user)
    if request.method == "POST":
        id = request.POST.get('id')
        try:
            hour = datetime.now().hour

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

            # setting necessary SellOrder fields

            user_portfolio.totalPortfolioAmount += sell_order.profit
            user_portfolio.investedAmount -= sell_order.cashAmount
            user_portfolio.liquidAmount = user_portfolio.totalPortfolioAmount - user_portfolio.investedAmount
            # updating UserPortfolio fields
            
            # #####################################  REMOVE FOR PRESENTATION/TESTING #####################################
            if hour < 9 or hour > 16:
                return redirect("order:outside-market-hours")
            # #####################################  REMOVE FOR PRESENTATION/TESTING #####################################

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

def insufficient_funds(request):
    return render(request, "insufficient-funds.html")

def not_market_hours(request):
    return render(request, "not-market-hours.html")