from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import UserPortfolio
from OrdersApp.models import SellOrders, BuyOrders

# Create your views here.
def signup_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user_portfolio = UserPortfolio()
            new_user_portfolio.username = form.data.get("username")
            new_user_portfolio.totalPortfolioAmount = 25_000
            # creating a new user portfolio for the new user
            # NOTE: when creating a super user, they must add their own portfolio through the interface admin if they intend to use the application with that account
            form.save()
            new_user_portfolio.save()
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
                # sends the user to the 
            else:
                return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_user(request):
    logout(request)
    return redirect("user:login")

def delete_account(request):
    username = request.user
    user = User.objects.get(username=username)
    user_portfolio = UserPortfolio.objects.get(username=username)
    sell_orders = SellOrders.objects.filter(user=username)
    buy_orders = BuyOrders.objects.filter(user=username)

    for buy in buy_orders: buy.delete()
    for sell in sell_orders: sell.delete()
    user_portfolio.delete()
    user.delete()
    return redirect("home")

# everything is basically handled here by django forms