import numpy as np
from django.db.models import Sum, Max, Avg
from OrdersApp.models import BuyOrders, SellOrders
from UsersApp.models import UserPortfolio

def collectStats(request):
    buy_orders = BuyOrders.objects.filter(user=request.user).order_by("-id")
    sell_orders = SellOrders.objects.filter(user=request.user).order_by("-id")

    total_profit = SellOrders.objects.filter(user=request.user).aggregate(total_profit=Sum('profit')).get("total_profit")

    max_profit = SellOrders.objects.filter(user=request.user).aggregate(max_profit=Max('profit')).get("max_profit")

    avg_profit = SellOrders.objects.filter(user=request.user).aggregate(avg_profit=Avg('profit')).get("avg_profit")

    buy_dates = [date[0] for date in sell_orders.values_list("buyDate")]

    sell_dates = [date[0] for date in sell_orders.values_list("sellDate")]

    buy_sell_date_list = [pair for pair in zip(sell_dates, buy_dates)]

    date_delta_list = [(sell - buy).days for sell, buy in buy_sell_date_list]

    avg_buy_sell_duration =  np.sum(date_delta_list) / len(date_delta_list)

    user_portfolio = UserPortfolio.objects.get(username=request.user)

    total_portfolio = user_portfolio.totalPortfolioAmount

    liquid_portfolio = user_portfolio.liquidAmount

    invested_portfolio = user_portfolio.investedAmount

    return {"buy_orders": buy_orders, "sell_orders": sell_orders, "total_profit": total_profit, "max_profit": max_profit, "avg_profit": avg_profit, 
            "avg_buy_sell_duration": avg_buy_sell_duration,"total_portfolio": total_portfolio, "liquid_portfolio": liquid_portfolio, "invested_portfolio": invested_portfolio}