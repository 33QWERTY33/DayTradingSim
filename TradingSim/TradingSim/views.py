from django.shortcuts import render

def home(request):
    # gather user information to display to page
    return render(request, "home.html", {"PLACEHOLDER": "PLACEHOLDER"})
