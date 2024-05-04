def handle_portfolio(request, rest=False, serializer=None):
    if request.method == "POST":
            new_user_portfolio = UserPortfolio()
            new_user_portfolio.username = form.data.get("username")
            new_user_portfolio.totalPortfolioAmount = 25_000
            # creating a new user portfolio for the new user
            # NOTE: when creating a super user, they must add their own portfolio through the interface admin if they intend to use the application with that account
            new_user_portfolio.save()