from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "taxi/index.html")

def bill(request):
    return render(request, "taxi/search_bill.html")

def driver(request):
    return render(request, "taxi/search_driv.html")

def taxi(request):
    return render(request, "taxi/search_taxi.html")

def trip(request):
    return render(request, "taxi/search_trip.html")

def user(request):
    return render(request, "taxi/search_user.html")