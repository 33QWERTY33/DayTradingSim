from django.shortcuts import render
from .utils import collectStats

def home(request):
    if request.user.is_authenticated:
        stats = collectStats(request)
        # data collection logic abstracted out to utils.py file
        return render(request, "home.html", {"stats": stats})
    else:
        return render(request, "home.html")

def info(request):
    return render(request, "info.html")
