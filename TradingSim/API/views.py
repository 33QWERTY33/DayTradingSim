from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from UsersApp.models import UserPortfolio
from OrdersApp.models import BuyOrders, SellOrders
from .serializers import BuyOrderSerializer, SellOrderSerializer, UserPortfolioSerializer

# Create your views here.
@api_view(["GET", "POST"])
def buy_orders(request, format=None):
    if request.method == "GET":
        orders = BuyOrders.objects.all()
        serializer = BuyOrderSerializer(orders, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = BuyOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "POST"])
def sell_orders(request, format=None):
    if request.method == "GET":
        orders = SellOrders.objects.all()
        serializer = SellOrderSerializer(orders, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = SellOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "POST"])
def user_portfolios(request, format=None):
    if request.method == "GET":
        portfolios = UserPortfolio.objects.all()
        serializer = UserPortfolioSerializer(portfolios, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = UserPortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def buy_order_by_id(request, id, format=None):
    try:
        order = BuyOrders.objects.get(id=id)
    except BuyOrders.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BuyOrderSerializer(order)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = BuyOrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(["GET", "PUT", "DELETE"])
def sell_order_by_id(request, id, format=None):
    try:
        order = SellOrders.objects.get(id=id)
    except SellOrders.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = SellOrderSerializer(order)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = BuyOrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(["GET", "PUT", "DELETE"])
def portfolio_by_username(request, user, format=None):
    try:
        portfolio = UserPortfolio.objects.get(username=user)
    except UserPortfolio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = UserPortfolioSerializer(portfolio)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = BuyOrderSerializer(portfolio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)