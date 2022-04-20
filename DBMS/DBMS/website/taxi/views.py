from django import forms
from django.shortcuts import render

class BillForm(forms.Form):
    bill_no = forms.IntegerField(label="Bill Number")
    user_id = forms.IntegerField(label="User_ID")
    amt = forms.IntegerField(label="Total Amount")

class DriverForm(forms.Form):
    trip_id = forms.IntegerField(label="Trip ID")
    name = forms.CharField(label = "Name")
    age = forms.IntegerField(label="Age")
    rating = forms.IntegerField(label="Rating")
    driver_id = forms.IntegerField(label="Driver ID")

class TaxiForm(forms.Form):
    driver_id = forms.IntegerField(label = "Driver ID")
    name = forms.CharField(label = "Name")
    car_id = forms.IntegerField(label="Car ID")

class TripForm(forms.Form):
    start = forms.CharField(label = "Start Location")
    end = forms.CharField(label = "Destination")
    bill_no = forms.IntegerField(label = "Bill Number")

class UserForm(forms.Form):
    name = forms.CharField(label = "Name")
    user_id = forms.IntegerField(label = "User ID")

# Create your views here.
def index(request):
    return render(request, "taxi/index.html")

def bill(request):
    return render(request, "taxi/search_bill.html", {
        "form": BillForm()
    })

def driver(request):
    return render(request, "taxi/search_driv.html", {
        "form": DriverForm()
    })

def taxi(request):
    return render(request, "taxi/search_taxi.html", {
        "form": TaxiForm()
    })

def trip(request):
    return render(request, "taxi/search_trip.html", {
        "form": TripForm()
    })

def user(request):
    return render(request, "taxi/search_user.html", {
        "form": UserForm()
    })