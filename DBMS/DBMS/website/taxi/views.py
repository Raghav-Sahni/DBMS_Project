#import mysql.connector
from pathlib import Path
from sqlite3 import dbapi2 as sq3
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Driver, BillDetails, CarManufacturer, CustomerService, PremiumUser, TripDetails, Taxi, Feedback

class BillForm(forms.Form):
    bill_no = forms.IntegerField(label="Bill Number", required=False)
    user_id = forms.IntegerField(label="User_ID", required=False)
    amt = forms.IntegerField(label="Total Amount", required=False)

class DriverForm(forms.Form):
    trip_id = forms.IntegerField(label="Trip ID", required=False)
    name = forms.CharField(label = "Name", required=False)
    age = forms.IntegerField(label="Age", required=False)
    rating = forms.IntegerField(label="Rating", required=False)
    driver_id = forms.IntegerField(label="Driver ID", required=False)

class TaxiForm(forms.Form):
    driver_id = forms.IntegerField(label = "Driver ID", required=False)
    name = forms.CharField(label = "Name", required=False)
    car_id = forms.IntegerField(label="Car ID", required=False)

class TripForm(forms.Form):
    start = forms.CharField(label = "Start Location", required=False)
    end = forms.CharField(label = "Destination", required=False)
    bill_no = forms.IntegerField(label = "Bill Number", required=False)

class UserForm(forms.Form):
    name = forms.CharField(label = "Name", required=False)
    user_id = forms.IntegerField(label = "User ID", required=False)

# Create your views here.
def index(request):
    return render(request, "taxi/index.html")

def bill(request):
    if request.method=="POST":
        form = BillForm(request.POST) #TO get data that user has submitted
        if form.is_valid(): #If submition is valid
            data = {"bill_no": form.cleaned_data["bill_no"], "user_id": form.cleaned_data["user_id"], "amount": form.cleaned_data["amt"]} #TaskForm stores task input in tasks variable
            
            b = BillDetails.objects.all()
            if data["bill_no"] != None:
                b = b.filter(bill_no = data["bill_no"])
            if data["user_id"] != None:
                b = b.filter(userid = data["user_id"])
            if data["amount"] != None:
                b = b.filter(tot_amount = data["amount"])
            return render(request, "taxi/table.html", {
                "data": b
            }) 
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
            #Still need to work on trip_id
            b = Driver.objects.all()
            if data["name"] != None:
                b = b.filter(name = data["name"])
            if data["age"] != None:
                b = b.filter(age = data["age"])
            if data["rating"] != None:
                b = b.filter(rating = data["rating"])
            if data["driver_id"] != None:
                b = b.filter(driver_id = data["driver_id"])
            return render(request, "taxi/table.html", {
                "data": b
            })
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
            #Still need to work name
            b = Driver.objects.all()
            t = Taxi.objects.all()
            if data["name"] != None:
                b = b.filter(name = data["name"])
                #t = t.filter(driver = b.values_list("driver_id"))

            if data["driver_id"] != None:
                t = t.filter(driver = data["driver_id"])
            if data["car_id"] != None:
                t = t.filter(car_id = data["car_id"])
            return render(request, "taxi/table.html", {
                "data": t
            })
            
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
            #Work on bill_no
            
            b = TripDetails.objects.all()
            if data["start"] != None:
                b = b.filter(startlocation = data["start"])
            if data["end"] != None:
                b = b.filter(destination = data["end"])
            return render(request, "taxi/table.html", {
                "data": b
            })
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

            b = User.objects.all()
            if data["name"] != None:
                b = b.filter(name = data["name"])
            if data["user_id"] != None:
                b = b.filter(userid = data["user_id"])
            return render(request, "taxi/table.html", {
                "data": b
            })
        else:# For server side validation, sometimes when we make a change here but client page has not been refreshed then the old version of the form may take invalid inputs this block is to prevent that
            return render(request, "taxi/search_user.html", {
                "form": form
            })

    return render(request, "taxi/search_user.html", {
        "form": UserForm()
    })