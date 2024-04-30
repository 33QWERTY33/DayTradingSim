from django.shortcuts import render
from .models import BuyOrders
# Create your views here.
def place_buy_order(request):
    return render(request, "place-buy-order.html")

def place_sell_order(request):
    currentOrders = BuyOrders.objects.filter(user=request.user).order_by("-buydate")

    return render(request, "place-sell-order.html", {"currentOrders": currentOrders})

def order_details(request, order):
    return render(request, "order-details.html", {"order": order})