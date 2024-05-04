from django.shortcuts import render, redirect
from .models import BuyOrders, SellOrders
from .handlers import handle_buy_order, handle_sell_order
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/user/login")
def place_buy_order(request):
    return handle_buy_order(request)
    # logic abstracted out to handlers.py to decrease repetition
    # This logic is also used in the REST API
    
@login_required(login_url="/user/login")
def place_sell_order(request):
    return handle_sell_order(request)
    # logic abstracted out to handlers.py to decrease repetition
    # This logic is also used in the REST API

def sell_order_details(request, id):
    order = SellOrders.objects.get(id=id)

    order.buyPrice = round(order.buyPrice, 2)
    order.cashAmount = round(order.cashAmount, 2)

    return render(request, "sell-order-details.html", {"order": order})

def buy_order_details(request, id):

    order = BuyOrders.objects.get(id=id)

    return render(request, "buy-order-details.html", {"order": order})

def insufficient_funds(request):
    return render(request, "insufficient-funds.html")

def not_market_hours(request):
    return render(request, "not-market-hours.html")