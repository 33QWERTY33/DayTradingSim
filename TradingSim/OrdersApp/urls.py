from django.urls import path
from .views import *

app_name = "order"

urlpatterns = [
    path("buy-order/", place_buy_order, name="buy-order"),
    path("sell-order/", place_sell_order, name="sell-order"),
    path("insufficient-funds/", insufficient_funds, name="insufficient-funds"),
    path("buy/<slug:id>", buy_order_details, name="buy-order-details"),
    path("sell/<slug:id>", sell_order_details, name="sell-order-details"),
]
# router for Orders App