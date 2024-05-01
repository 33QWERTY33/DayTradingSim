from django.db import models

# Create your models here.
class BuyOrders(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50)
    ticker = models.CharField(max_length=5)
    buyPrice = models.FloatField()
    cashAmount = models.FloatField()
    stockAmount = models.FloatField()
    sellTrigger = models.FloatField()
    buyDate = models.DateField()
    totalPercentage = None

    def __str__(self):
        return f"{self.user} bought {self.stockAmount} shares of {self.ticker} for {self.cashAmount}"


class SellOrders(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=50)
    ticker = models.CharField(max_length=5)
    buyPrice = models.FloatField()
    cashAmount = models.FloatField()
    stockAmount = models.FloatField()
    sellPrice = models.FloatField()
    profit = models.FloatField()
    buyDate = models.DateField(default="1950-1-1")
    sellDate = models.DateField(default="1950-1-1")
    totalPercentage = None

    def __str__(self):
        return f"{self.user} sold {self.stockAmount} shares of {self.ticker} for {self.profit} profit"

'''
    CurrentMarketOrders schema:
    orderID: auto incrementing Primary key of CurrentMarketOrders model
    user: get the current user and add that value automatically to this row
    ticker: get the ticker symbol that they inputted in the form to place the order
    buyprice: the price that the stock was bought at
    cashAmount: will be a float storing the cash amount used to purchase the stocks
    stockAmount: will be a float storing the amount of stocks the order gained the user
    sellTrigger: will be a float storing the price at which the user will automatically sell the stock
    buydate: the date the order was placed on to assist with data vis for user

    CompleteMarketOrders schema:
    orderID: data will be transferred from user field of CurrentMarketOrders upon transfer
    user: data will be transferred from user field of CurrentMarketOrders upon transfer
    ticker: data will be transferred from user field of CurrentMarketOrders upon transfer
    buyprice: data will be transferred from user field of CurrentMarketOrders upon transfer
    cashAmount: data will be transferred from user field of CurrentMarketOrders upon transfer
    stockAmount: data will be transferred from user field of CurrentMarketOrders upon transfer
    sellprice: sell price will be set whenever the user puts in a sell order
    profit: will be an aggregate value of (sellprice * stockAmount) - cashAmount
    buyDate: data will be transferred from user field of CurrentMarketOrders upon transfer
    sellDate: will be a date value set by whatever the date is either when the stock price first hit the sell trigger, or when the stock is manually sold

'''