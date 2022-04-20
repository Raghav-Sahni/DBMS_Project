from django.contrib import admin

from .models import User, Driver, BillDetails, CarManufacturer, CustomerService, PremiumUser, TripDetails, Taxi, Feedback
# Register your models here.

admin.site.register(User)
admin.site.register(BillDetails)
admin.site.register(CarManufacturer)
admin.site.register(PremiumUser)
admin.site.register(TripDetails)
admin.site.register(Taxi)
admin.site.register(Feedback)

