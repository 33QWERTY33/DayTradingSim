from django.db import models

# Create your models here.
class UserPortfolio(models.Model):
    username = models.CharField(primary_key=True, max_length=100)
    totalPortfolioAmount = models.FloatField(default=25_000)
    liquidAmount = models.FloatField(default=25_000)
    investedAmount = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.username}'s portfolio details"
    
'''
    UserPortfolio Schema:
        username: will be set to request.user
        totalPortfolioAmount: by default is set to 25,000 in appropriate view (no default cause there could be a tier system in the future)
        liquidAmount: spendable money, basically totalPortfolioAmount - investedAmount
        investedAmount: the amount of money that's invested currently, basically a sum of all the BuyOrder cashAmounts tied to that user
'''