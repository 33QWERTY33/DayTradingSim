from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import UserPortfolio

# Create your views here.
def signup_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print("FORM CREATED")
        if form.is_valid():
            new_user_portfolio = UserPortfolio()
            new_user_portfolio.username = form.data.get("username")
            new_user_portfolio.portfolioAmount = 25_000
            print("FORM WAS VALID")
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
    # user.delete()
    return redirect("home")