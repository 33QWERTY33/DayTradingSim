from rest_framework import serializers
from OrdersApp.models import BuyOrders, SellOrders
from UsersApp.models import UserPortfolio


class SellOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellOrders
        fields = '__all__'

class BuyOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyOrders
        fields = '__all__'

class UserPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPortfolio
        fields = '__all__'