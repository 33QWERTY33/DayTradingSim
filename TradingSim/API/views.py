from rest_framework.response import Response
from rest_framework.decorators import api_view

from UsersApp.models import UserPortfolio
from OrdersApp.models import BuyOrders, SellOrders
from .serializers import BuyOrderSerializer, SellOrderSerializer, UserPortfolioSerializer

# Create your views here.
@api_view(["GET"])
def buy_orders(request, format=None):
    orders = BuyOrders.objects.all()
    serializer = BuyOrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def sell_orders(request, format=None):
    orders = SellOrders.objects.all()
    serializer = SellOrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def user_portfolios(request, format=None):
    portfolios = UserPortfolio.objects.all()
    serializer = UserPortfolioSerializer(portfolios, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def buy_order_by_id(request, id, format=None):
    orders = BuyOrders.objects.get(id=id)
    serializer = BuyOrderSerializer(orders, many=False)
    print("#"*100, serializer)
    return Response(serializer.data)

@api_view(["GET"])
def sell_order_by_id(request, id, format=None):
    orders = SellOrders.objects.get(id=id)
    serializer = SellOrderSerializer(orders, many=False)
    return Response(serializer.data)

@api_view(["GET"])
def portfolio_by_username(request, user, format=None):
    portfolios = UserPortfolio.objects.get(username=user)
    serializer = UserPortfolioSerializer(portfolios, many=False)
    return Response(serializer.data)



# NOTE: researching djangorestframework module.