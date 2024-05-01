from django.shortcuts import render
from .utils import collectStats

def home(request):
    stats = collectStats(request)
    # data collection logic abstracted out to utils.py file
    return render(request, "home.html", {"stats": stats})

def info(request):
    return render(request, "info.html")
