from django.db import models

class User(models.Model):
    userid = models.IntegerField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    user_email = models.CharField(db_column='User_email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contact_no = models.CharField(db_column='Contact_No', max_length=30, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=30, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'

class BillDetails(models.Model):
    bill_no = models.IntegerField(db_column='Bill_no', primary_key=True)  # Field name made lowercase.
    date_bill = models.CharField(max_length=20, blank=True, null=True)
    tot_amt = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tripid = models.IntegerField(db_column='TripID')  # Field name made lowercase.
    payment_mode = models.CharField(db_column='Payment_mode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill_details'


class CarManufacturer(models.Model):
    car_id = models.IntegerField(db_column='Car_ID', blank=True, null=True)  # Field name made lowercase.
    registrationid = models.CharField(db_column='RegistrationId', max_length=30, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=30, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    car_type = models.CharField(db_column='Car_type', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'car_manufacturer'


class CustomerService(models.Model):
    employ_id = models.IntegerField(db_column='Employ_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contact_no = models.CharField(db_column='Contact_No', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer_service'


class Driver(models.Model):
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contact_no = models.CharField(db_column='Contact_No', max_length=30, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    driver_id = models.IntegerField(db_column='Driver_ID', primary_key=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'driver'

class PremiumUser(models.Model):
    userid = models.ForeignKey('User', db_column='UserID', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'premium_user'

class Taxi(models.Model):
    taxi_id = models.IntegerField(db_column='Taxi_id', primary_key=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    driver = models.ForeignKey(Driver, db_column='Driver_ID', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    car_id = models.IntegerField(blank=True, null=True)

    def __str__(self): 
        return f"ID: {self.taxi_id}, Status: {self.status}, Driver: {self.driver}, CarID: {self.car_id}"

    class Meta:
        managed = False
        db_table = 'taxi'


class TripDetails(models.Model):
    tripid = models.IntegerField(db_column='TripID', blank=True, null=True)  # Field name made lowercase.
    tripamount = models.FloatField(db_column='TripAmount', blank=True, null=True)  # Field name made lowercase.
    starttime = models.TextField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.TextField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    taxi_id = models.IntegerField(db_column='Taxi_ID', blank=True, null=True)  # Field name made lowercase.
    pool_num = models.IntegerField(db_column='Pool_num', blank=True, null=True)  # Field name made lowercase.
    startlocation = models.TextField(db_column='StartLocation', blank=True, null=True)  # Field name made lowercase.
    destination = models.TextField(db_column='Destination', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', on_delete=models.CASCADE, db_column='UserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trip_details'

class Feedback(models.Model):
    feedback = models.CharField(db_column='Feedback', max_length=30, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', db_column='UserID', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    bill_no = models.ForeignKey(BillDetails, db_column='Bill_no', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    employ = models.ForeignKey(CustomerService, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'feedback'

