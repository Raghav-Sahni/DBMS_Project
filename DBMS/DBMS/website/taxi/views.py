#import mysql.connector
from pathlib import Path
from sqlite3 import dbapi2 as sq3
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Driver, BillDetails, CarManufacturer, CustomerService, PremiumUser, TripDetails, Taxi, Feedback

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
    if request.method=="POST":
        form = BillForm(request.POST) #TO get data that user has submitted
        if form.is_valid(): #If submition is valid
            data = {"bill_no": form.cleaned_data["bill_no"], "user_id": form.cleaned_data["user_id"], "amount": form.cleaned_data["amt"]} #TaskForm stores task input in tasks variable
            #request.session["tasks"]+=[task]
            b = BillDetails.objects.filter(bill_no = data["bill_no"], tot_amt = data["amount"], userid = data["user_id"])
            return render(request, "taxi/table.html", {
                "data": b
            }) # Directs me back to view tasks after submiting query
        else:# For server side validation, sometimes when we make a change here but client page has not been refreshed then the old version of the form may take invalid inputs this block is to prevent that
            return render(request, "taxi/search_bill.html", {
                "form": form
            })

    return render(request, "taxi/search_bill.html", {
        "form": BillForm()
    })

def driver(request):
    if request.method=="POST":
        form = DriverForm(request.POST) #TO get data that user has submitted
        if form.is_valid(): #If submition is valid
            data = {"trip_id": form.cleaned_data["trip_id"], "name": form.cleaned_data["name"], "age": form.cleaned_data["age"], "rating": form.cleaned_data["rating"], "driver_id": form.cleaned_data["driver_id"]} #TaskForm stores task input in tasks variable
            #request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse("taxi:index")) # Directs me back to view tasks after submiting query
        else:# For server side validation, sometimes when we make a change here but client page has not been refreshed then the old version of the form may take invalid inputs this block is to prevent that
            return render(request, "taxi/search_bill.html", {
                "form": form
            })

    return render(request, "taxi/search_driv.html", {
        "form": DriverForm()
    })

def taxi(request):
    if request.method=="POST":
        form = TaxiForm(request.POST) #TO get data that user has submitted
        if form.is_valid(): #If submition is valid
            data = {"driver_id": form.cleaned_data["driver_id"], "name": form.cleaned_data["name"], "car_id": form.cleaned_data["car_id"]} #TaskForm stores task input in tasks variable
            #request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse("taxi:index")) # Directs me back to view tasks after submiting query
        else:# For server side validation, sometimes when we make a change here but client page has not been refreshed then the old version of the form may take invalid inputs this block is to prevent that
            return render(request, "taxi/search_taxi.html", {
                "form": form
            })

    return render(request, "taxi/search_taxi.html", {
        "form": TaxiForm()
    })

def trip(request):
    if request.method=="POST":
        form = TripForm(request.POST) #TO get data that user has submitted
        if form.is_valid(): #If submition is valid
            data = {"start": form.cleaned_data["start"], "end": form.cleaned_data["end"], "bill_no": form.cleaned_data["bill_no"]} #TaskForm stores task input in tasks variable
            #request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse("taxi:index")) # Directs me back to view tasks after submiting query
        else:# For server side validation, sometimes when we make a change here but client page has not been refreshed then the old version of the form may take invalid inputs this block is to prevent that
            return render(request, "taxi/search_trip.html", {
                "form": form
            })

    return render(request, "taxi/search_trip.html", {
        "form": TripForm()
    })

def user(request):
    if request.method=="POST":
        form = UserForm(request.POST) #TO get data that user has submitted
        if form.is_valid(): #If submition is valid
            data = {"name": form.cleaned_data["name"], "user_id":form.cleaned_data["user_id"]} #TaskForm stores task input in tasks variable
            #request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse("taxi:index")) # Directs me back to view tasks after submiting query
        else:# For server side validation, sometimes when we make a change here but client page has not been refreshed then the old version of the form may take invalid inputs this block is to prevent that
            return render(request, "taxi/search_user.html", {
                "form": form
            })

    return render(request, "taxi/search_user.html", {
        "form": UserForm()
    })