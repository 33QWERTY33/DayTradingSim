from django.db import models

# Create your models here.
class UserPortfolio(models.Model):
    username = models.CharField(primary_key=True, max_length=100)
    totalPortfolioAmount = models.FloatField()
    liquidAmount = models.FloatField(default=25_000)
    investedAmount = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.username}'s portfolio details"