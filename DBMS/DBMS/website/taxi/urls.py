from django.urls import path
from . import views

app_name = "taxi"
urlpatterns = [
    path("", views.index, name="index"),
    path("bill/", views.bill, name="bill"),
    path("driver/", views.driver, name="driver"),
    path("taxi/", views.taxi, name="taxi"),
    path("trip/", views.trip, name="trip"),
    path("user/", views.user, name="user")
]