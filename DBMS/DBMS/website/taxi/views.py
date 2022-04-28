from pathlib import Path
import re
from sqlite3 import dbapi2 as sq3
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Driver, BillDetails, CarManufacturer, CustomerService, PremiumUser, TripDetails, Taxi, Feedback
from django.db import connection

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

class AddUserForm(forms.Form):
    name = forms.CharField(label = "Name", required=False)
    user_id = forms.IntegerField(label = "User ID", required=False)
    contact_no= forms.IntegerField(label="Contact_No", required=False)
    gender=forms.CharField(label="Gender", required=False)
    address = forms.CharField(label="Address", required=False)
    User_email= forms.CharField(label="User_email", required=False)

class AddTaxiForm(forms.Form):
    taxi_id = forms.IntegerField(label='Taxi ID', required=False)  # Field name made lowercase.
    status = forms.CharField(label='Status', required=False)  # Field name made lowercase.
    driver_id = forms.IntegerField(label='Driver ID', required=False)  # Field name made lowercase.
    car_id = forms.IntegerField(label="Car ID", required=False)

class AddDriverForm(forms.Form):
    name = forms.CharField(label='Name', required=False)  # Field name made lowercase.
    gender = forms.CharField(label='Gender', required=False)  # Field name made lowercase.
    contact_no = forms.CharField(label='Contact_No', required=False)  # Field name made lowercase.
    age = forms.IntegerField(label='Age', required=False)  # Field name made lowercase.
    driver_id = forms.IntegerField(label='Driver_ID', required=False)  # Field name made lowercase.
    rating = forms.IntegerField(label='Rating', required=False) # Field name made lowercase.

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
            d = Driver.objects.all()
            if data["trip_id"] != None:
                c = connection.cursor()
                c.execute("SELECT * FROM DRIVER WHERE Driver_ID in (SELECT Driver_ID from TAXI WHERE Taxi_ID in(SELECT Taxi_ID FROM TRIP_DETAILS WHERE TripID =\'"+str(data["trip_id"])+"\'))")
                return render(request, "taxi/table.html", {
                "data": c.fetchall()
            })
            if data["name"] != "":
                d = d.filter(name = data["name"])
            if data["age"] != None:
                d = d.filter(age = data["age"])
            if data["rating"] != None:
                d = d.filter(rating = data["rating"])
            if data["driver_id"] != None:
                d = d.filter(driver_id = data["driver_id"])
            return render(request, "taxi/table.html", {
                "data": d
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
            t = Taxi.objects.all()
            if data["name"] != "":
                c = connection.cursor()
                c.execute("SELECT * FROM Taxi WHERE Driver_ID IN(SELECT driver_id FROM Driver WHERE name =\'"+data["name"]+"\')")
                return render(request, "taxi/table.html", {
                "data": c.fetchall()
            })
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
            if data["bill_no"] != None:
                c = connection.cursor()
                c.execute("SELECT * FROM TRIP_DETAILS WHERE TripID in (SELECT TripID FROM BILL_DETAILS WHERE Bill_No = \'"+str(data["bill_no"])+"\')")
                return render(request, "taxi/table.html", {
                "data": c.fetchall()
            })
            
            b = TripDetails.objects.all()
            if data["start"] != "":
                b = b.filter(startlocation = data["start"])
            if data["end"] != "":
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
            if data["name"] != "":
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

def premium_user(request):
    c = connection.cursor()
    c.execute("select P.UserID, U.Name from PREMIUM_USER P, USER U, TRIP_DETAILS T where P.UserID=T.UserID and T.UserID=U.UserID")
    
    return render(request, "taxi/premium_user.html", {
        "data": c.fetchall()
})

def example_(request):

    
    c = connection.cursor()
    c.execute("select max(UserID) from user")
    return render(request, "taxi/output.html", {
        "data": c.fetchall()
})

def add_user(request):
    if request.method=="POST":
        form = AddUserForm(request.POST) #TO get data that user has submitted
        if form.is_valid(): #If submition is valid
            
            data = {"name": form.cleaned_data["name"], "user_id":form.cleaned_data["user_id"], "contact_no":form.cleaned_data["contact_no"], "gender":form.cleaned_data["gender"],"address":form.cleaned_data["address"], "User_email":form.cleaned_data["User_email"]}  #TaskForm stores task input in tasks variable
            c = connection.cursor()
            c.execute("INSERT INTO USER VALUES(\'"+str(data["user_id"])+"\',\'"+str(data["User_email"])+"\',\'"+str(data["contact_no"])+"\',\'"+str(data["name"])+"\',\'"+str(data["gender"])+"\',\'"+str(data["address"])+"\')")
            #c.commit()
    return render(request, "taxi/add_user.html", {
        "form": AddUserForm()
    })

def add_taxi(request):
    if request.method=="POST":
        form = AddTaxiForm(request.POST) #TO get data that user has submitted
        if form.is_valid(): #If submition is valid
            
            data = {"taxi_id": form.cleaned_data["taxi_id"], "status":form.cleaned_data["status"], "driver_id":form.cleaned_data["driver_id"], "car_id":form.cleaned_data["car_id"]}  #TaskForm stores task input in tasks variable
            c = connection.cursor()
            c.execute("INSERT INTO TAXI VALUES("+str(data["taxi_id"])+",\'"+str(data["status"])+"\',"+str(data["driver_id"])+","+str(data["car_id"])+")")
    return render(request, "taxi/add_taxi.html", {
        "form": AddTaxiForm()
    })

def add_driver(request):
    if request.method=="POST":
        form = AddDriverForm(request.POST) #TO get data that user has submitted
        if form.is_valid(): #If submition is valid
            
            data = {"name": form.cleaned_data["name"], "driver_id":form.cleaned_data["driver_id"], "contact_no":form.cleaned_data["contact_no"], "gender":form.cleaned_data["gender"],"age":form.cleaned_data["age"], "rating":form.cleaned_data["rating"]}  #TaskForm stores task input in tasks variable
            c = connection.cursor()
            c.execute("INSERT INTO DRIVER VALUES(\'"+str(data["name"])+"\',\'"+str(data["gender"])+"\',\'"+str(data["contact_no"])+"\',\'"+str(data["age"])+"\',\'"+str(data["driver_id"])+"\',\'"+str(data["rating"])+"\')")
            #c.commit()
    return render(request, "taxi/add_driver.html", {
        "form": AddDriverForm()
    })



    
