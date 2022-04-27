from django.urls import path
from . import views

app_name = "taxi"
urlpatterns = [
    path("", views.index, name="index"),
    path("bill/", views.bill, name="bill"),
    path("driver/", views.driver, name="driver"),
    path("taxi/", views.taxi, name="taxi"),
    path("trip/", views.trip, name="trip"),
    path("user/", views.user, name="user"),
    path("example_/", views.example_, name="example_"),
    path("add_user/", views.add_user, name="add_user"),
    path("add_taxi/", views.add_taxi, name="add_taxi"),
    path("add_driver/", views.add_driver, name="add_driver")
]