from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "api"

urlpatterns = [
    path("get-buy-orders", buy_orders),
    path("get-sell-orders", sell_orders),
    path("get-portfolios", user_portfolios),
    path("buy-order/<int:id>", buy_order_by_id),
    path("sell-order/<int:id>", sell_order_by_id),
    path("portfolio/<str:user>", portfolio_by_username),
]

urlpatterns = format_suffix_patterns(urlpatterns)