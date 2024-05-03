from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from TradingSim.views import *
from TickerApp import urls
from UsersApp import urls
from OrdersApp import urls
from LeaderboardApp import urls
from API import urls

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", home, name="home"),
    path("info/", info, name="info"),
    path("ticker/", include('TickerApp.urls')),
    path("user/", include('UsersApp.urls')),
    path("order/", include('OrdersApp.urls')),
    path("leaderboard/", include("LeaderboardApp.urls")),
    path("api/", include('API.urls')),
    re_path(r".*", page_not_found, name="404")
]
# master router for the project
