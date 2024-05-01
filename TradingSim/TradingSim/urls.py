"""
URL configuration for TradingSim project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from TradingSim.views import home, info
from TickerApp import urls
from UsersApp import urls
from OrdersApp import urls

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", home, name="home"),
    path("info/", info, name="info"),
    path("ticker/", include('TickerApp.urls')),
    path("user/", include('UsersApp.urls')),
    path("order/", include('OrdersApp.urls'))
]
# master router for the project