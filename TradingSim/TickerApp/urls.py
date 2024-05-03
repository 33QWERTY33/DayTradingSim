from django.urls import path
from .views import *

app_name = 'ticker'

urlpatterns = [
    path("", get_ticker, name="get-ticker"),
    path("display-ticker-info/", display_ticker_info, name="ticker-info"),
    path("incorrect-ticker", incorrect_ticker, name="incorrect-ticker")
]
# router for Ticker App