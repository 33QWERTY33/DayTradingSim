from django.shortcuts import render
from OrdersApp.models import BuyOrders, SellOrders

def home(request):
    buy_orders = BuyOrders.objects.filter(user=request.user).order_by("-buydate")
    sell_orders = SellOrders.objects.filter(user=request.user).order_by("-buydate")
    return render(request, "home.html", {"buy_orders": buy_orders, "sell_orders": sell_orders})

def info(request):
    # gather user information to display to page
    return render(request, "info.html")
