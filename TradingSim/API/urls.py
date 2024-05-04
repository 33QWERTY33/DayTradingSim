from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "api"

urlpatterns = [
    path("CR-buy-orders", buy_orders),
    path("CR-sell-orders", sell_orders),
    path("CR-portfolios", user_portfolios),
    path("RUD-buy-order/<int:id>", buy_order_by_id),
    path("RUD-sell-order/<int:id>", sell_order_by_id),
    path("RUD-portfolio/<str:user>", portfolio_by_username),
]

urlpatterns = format_suffix_patterns(urlpatterns)