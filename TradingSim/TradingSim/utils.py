import numpy as np
from django.db.models import Sum, Max, Avg
from OrdersApp.models import BuyOrders, SellOrders
from UsersApp.models import UserPortfolio
import matplotlib.pyplot as plt
import os

def collectStats(request):
    buy_orders = BuyOrders.objects.filter(user=request.user).order_by("-id")
    sell_orders = SellOrders.objects.filter(user=request.user).order_by("-id")

    total_profit = SellOrders.objects.filter(user=request.user).aggregate(total_profit=Sum('profit')).get("total_profit")

    max_profit = SellOrders.objects.filter(user=request.user).aggregate(max_profit=Max('profit')).get("max_profit")

    avg_profit = SellOrders.objects.filter(user=request.user).aggregate(avg_profit=Avg('profit')).get("avg_profit")

    buy_dates = [date[0] for date in sell_orders.values_list("buyDate")]

    sell_dates = [date[0] for date in sell_orders.values_list("sellDate")]
    # get lists of datetime.date objects
    buy_sell_date_list = [pair for pair in zip(sell_dates, buy_dates)]
    # zip lists
    date_delta_list = [(sell - buy).days for sell, buy in buy_sell_date_list]
    # use datetime.date.__sub__ to find the difference, then take the days attribute of the result obj for pair in buy_sell_date_list
    avg_buy_sell_duration =  np.sum(date_delta_list) / len(date_delta_list)
    # finding the average... I thought I'd have way more uses for numpy
    user_portfolio = UserPortfolio.objects.get(username=request.user)

    total_portfolio = user_portfolio.totalPortfolioAmount

    liquid_portfolio = user_portfolio.liquidAmount

    invested_portfolio = user_portfolio.investedAmount

    liquid_percent = round((liquid_portfolio / total_portfolio) * 100, 2)
    invested_percent = round((invested_portfolio / total_portfolio) * 100, 2)

    for order in buy_orders:
        order.totalPercentage = round((order.cashAmount / total_portfolio) * 100, 2)

    for order in sell_orders:
        order.totalPercentage = round((order.profit / total_profit) * 100, 2)

    orders = [order for order in sell_orders]

    profits = [profit.profit for profit in orders]

    dates = [date.sellDate.strftime('%Y-%m-%d') for date in orders]

    plt.style.use('dark_background')

    plt.figure(figsize=(15, 10))

    plt.bar(dates, profits)

    plt.title("Profits by Date")

    plt.xlabel("Date")
    plt.ylabel("Profit")

    plt.savefig(os.path.join("static", "assets", "userStats", "profitReport.png"))

    return {"buy_orders": buy_orders, "sell_orders": sell_orders, "total_profit": total_profit, "max_profit": max_profit, "avg_profit": avg_profit, 
            "avg_buy_sell_duration": avg_buy_sell_duration,"total_portfolio": total_portfolio, "liquid_portfolio": liquid_portfolio,
            "invested_portfolio": invested_portfolio, "liquid_percent": liquid_percent, "invested_percent":invested_percent}