from django.shortcuts import render
from OrdersApp.models import BuyOrders, SellOrders
from django.db.models import Sum, Max, Avg
from datetime import datetime
import numpy as np

def home(request):
    buy_orders = BuyOrders.objects.filter(user=request.user).order_by("-buyDate")
    sell_orders = SellOrders.objects.filter(user=request.user).order_by("-buyDate")

    total_profit = SellOrders.objects.aggregate(total_profit=Sum('profit')).get("total_profit")

    max_profit = SellOrders.objects.aggregate(max_profit=Max('profit')).get("max_profit")

    avg_profit = SellOrders.objects.aggregate(avg_profit=Avg('profit')).get("avg_profit")

    buy_dates = [date[0] for date in sell_orders.values_list("buyDate")]

    sell_dates = [date[0] for date in sell_orders.values_list("sellDate")]

    buy_sell_date_list = [pair for pair in zip(sell_dates, buy_dates)]

    date_delta_list = [(sell - buy).days for sell, buy in buy_sell_date_list]

    avg_buy_sell_duration =  np.sum(date_delta_list) / len(date_delta_list)

    stats = {"total_profit": total_profit, "max_profit": max_profit, "avg_profit": avg_profit, "avg_buy_sell_duration": avg_buy_sell_duration}

    return render(request, "home.html", {"buy_orders": buy_orders, "sell_orders": sell_orders, "stats": stats})

def info(request):
    return render(request, "info.html")
