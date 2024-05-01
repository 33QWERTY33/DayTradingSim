from django.shortcuts import render
from UsersApp.models import UserPortfolio

def leaderboard_view(request):
    portfolios = UserPortfolio.objects.all().order_by("-totalPortfolioAmount")

    portfolio_totals = [(user.username, user.totalPortfolioAmount) for user in portfolios]

    return render(request, "leaderboard.html", {"results":portfolio_totals})