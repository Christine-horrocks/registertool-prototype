from django.urls import path
from . import views

app_name = "dev_con"

urlpatterns = [
    path("", views.pick_csv, name="pick_csv")
]
