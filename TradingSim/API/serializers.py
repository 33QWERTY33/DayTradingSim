from rest_framework import serializers
from OrdersApp.models import BuyOrders, SellOrders
from UsersApp.models import UserPortfolio


class GetSellOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellOrders
        fields = '__all__'

class GetBuyOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyOrders
        fields = "__all__"

class GetUserPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPortfolio
        fields = '__all__'

class PostSellOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellOrders
        fields = ["id"]

class PostBuyOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyOrders
        fields = ["user", "ticker", "stockAmount"]

class PostUserPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPortfolio
        fields = ["username", "totalPortfolioAmount"]