from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status

from yfinance.base import TickerBase
from UsersApp.models import UserPortfolio
from OrdersApp.models import SellOrders, BuyOrders
from datetime import datetime

def handle_buy_order(request, rest=False, serializer=None):
    if rest:
        user_portfolio = UserPortfolio.objects.get(username=request.data.get("user"))
    else:
        user_portfolio = UserPortfolio.objects.get(username=request.user)

    if request.method == "POST":
        try:
            hour = datetime.now().hour

            new_buy_order = BuyOrders()

            if rest:
                new_buy_order.user = request.data.get("user")
                new_buy_order.ticker = request.data.get("ticker").upper()
                new_buy_order.stockAmount = float(request.data.get("stockAmount"))
            else:
                new_buy_order.user = request.POST.get("username")
                new_buy_order.ticker = request.POST.get("ticker").upper()
                new_buy_order.stockAmount = float(request.POST.get("stockAmount"))

            new_buy_order.buyPrice = float(TickerBase(new_buy_order.ticker).get_info().get("currentPrice") or TickerBase(new_buy_order.ticker).get_info().get("navPrice"))
            new_buy_order.cashAmount = new_buy_order.buyPrice * new_buy_order.stockAmount
            new_buy_order.buyDate = datetime.now().date()

            # setting BuyOrders necessary fields

            if new_buy_order.cashAmount > user_portfolio.liquidAmount:
                if rest:
                    return Response(status=status.HTTP_412_PRECONDITION_FAILED)
                else:
                    return redirect("order:insufficient-funds")
            # broke people land

            # #####################################  REMOVE FOR PRESENTATION/TESTING #####################################
            # if hour < 9 or hour > 16:
            #     if rest:
            #         return Response(status=status.HTTP_412_PRECONDITION_FAILED)
            #     else:
            #         return redirect("order:outside-market-hours")
            # #####################################  REMOVE FOR PRESENTATION/TESTING #####################################

            user_portfolio.investedAmount += new_buy_order.cashAmount
            user_portfolio.liquidAmount = user_portfolio.totalPortfolioAmount - user_portfolio.investedAmount
            # updating UserPortfolio fields

            user_portfolio.save()
            new_buy_order.save()
        except ZeroDivisionError:
            if rest:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return redirect("ticker:incorrect-ticker")
        if rest:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return redirect("home")
    if rest:
        return Response(serializer.data)
    else:    
        return render(request, "place-buy-order.html", {"portfolio": user_portfolio})
    

def handle_sell_order(request, rest=False, serializer=None):
    if request.method == "POST":
        if rest:
            id=request.data.get("id")
        else:
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

            user_portfolio = UserPortfolio.objects.get(username=sell_order.user)

            # setting necessary SellOrder fields

            user_portfolio.totalPortfolioAmount += sell_order.profit
            user_portfolio.investedAmount -= sell_order.cashAmount
            user_portfolio.liquidAmount = user_portfolio.totalPortfolioAmount - user_portfolio.investedAmount
            # updating UserPortfolio fields
            
            # #####################################  REMOVE FOR PRESENTATION/TESTING #####################################
            # if hour < 9 or hour > 16:
            #     if rest:
            #         return Response(status=status.HTTP_412_PRECONDITION_FAILED)
            #     else:
            #         return redirect("order:outside-market-hours")
            # #####################################  REMOVE FOR PRESENTATION/TESTING #####################################

            buy_order.delete()
            user_portfolio.save()
            sell_order.save()
        except:
            if rest:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return redirect("ticker:incorrect-ticker")
        if rest:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return redirect("home")

    currentOrders = BuyOrders.objects.filter(user=request.user).order_by("-buyDate")

    if rest:
        return Response(serializer.data)
    else:
        return render(request, "place-sell-order.html", {"currentOrders": currentOrders, "portfolio":user_portfolio})

# this file is not pretty... I almost wish I had just written the logic all over again inside of the API app