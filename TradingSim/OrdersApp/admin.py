from django.contrib import admin
from .models import CurrentMarketOrders, CompleteMarketOrders

# Register your models here.
admin.site.register(CurrentMarketOrders)
admin.site.register(CompleteMarketOrders)