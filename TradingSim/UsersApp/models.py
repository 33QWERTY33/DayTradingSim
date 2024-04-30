from django.db import models

# Create your models here.
class UserPortfolio(models.Model):
    username = models.CharField(primary_key=True, max_length=100)
    portfolioAmount = models.FloatField()