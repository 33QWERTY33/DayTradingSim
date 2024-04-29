from django.shortcuts import render

def log_in(request):
    return render(request, "login.html")

def home(request):
    # gather user information to display to page
    return render(request, "home.html", {"PLACEHOLDER": "PLACEHOLDER"})
