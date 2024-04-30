from django.db import models

# Create your models here.
class CurrentMarketOrders(models.Model):
    user = models.CharField(max_length=50)
    ticker = models.CharField(max_length=5)
    buyprice = models.FloatField()
    cashAmount = models.FloatField()
    stockAmount = models.FloatField()
    pending = models.BooleanField()
    buydate = models.DateField()

    def __str__(self):
        return f"{self.user} bought {self.stockAmount} shares of {self.ticker} for {self.cashAmount}"


class CompleteMarketOrders(models.Model):
    user = models.CharField(max_length=50)
    ticker = models.CharField(max_length=5)
    buyprice = models.FloatField()
    cashAmount = models.FloatField()
    stockAmount = models.FloatField()
    sellPrice = models.FloatField()
    profit = models.FloatField()

    def __str__(self):
        return f"{self.user} sold {self.stockAmount} shares of {self.ticker} for {self.profit} profit"

'''
    CurrentMarketOrders schema:
    user: get the current user and add that value automatically to this row
    ticker: get the ticker symbol that they inputted in the form to place the order
    buyprice: the price that the stock was bought at
    cashAmount: will be a float storing the cash amount used to purchase the stocks
    stockAmount: will be a float storing the amount of stocks the order gained the user
    pending: pending is a bool, when set to false remove the record from CurrentMarketOrders and place in CompleteMarketOrders where sellprice and profit fields will be added
    buydate: the date the order was placed on to assist with data vis for user

    CompleteMarketOrders schema:
    user: data will be transferred from user field of CurrentMarketOrders upon transfer
    ticker: data will be transferred from user field of CurrentMarketOrders upon transfer
    buyprice: data will be transferred from user field of CurrentMarketOrders upon transfer
    cashAmount: data will be transferred from user field of CurrentMarketOrders upon transfer
    stockAmount: data will be transferred from user field of CurrentMarketOrders upon transfer
    sellprice: sell price will be set whenever the user puts in a sell order
    profit: will be an aggregate value of (sellprice * stockAmount) - cashAmount

'''