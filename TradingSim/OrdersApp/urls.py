from django.urls import path
from .views import place_buy_order, place_sell_order, buy_order_details, sell_order_details

app_name = "order"

urlpatterns = [
    path("buy-order/", place_buy_order, name="buy-order"),
    path("sell-order/", place_sell_order, name="sell-order"),
    path("buy/<slug:id>", buy_order_details, name="buy-order-details"),
    path("sell/<slug:id>", sell_order_details, name="sell-order-details")
]