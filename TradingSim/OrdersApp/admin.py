from django.contrib import admin
from .models import BuyOrders, SellOrders

# Register your models here.
admin.site.register(BuyOrders)
admin.site.register(SellOrders)