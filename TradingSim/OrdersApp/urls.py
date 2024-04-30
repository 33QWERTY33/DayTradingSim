from django.urls import path
from .views import place_buy_order, place_sell_order, order_details

app_name = "order"

urlpatterns = [
    path("buy-order/", place_buy_order, name="buy-order"),
    path("sell-order/", place_sell_order, name="sell-order"),
    path("<slug:id>", order_details, name="order-details")
]