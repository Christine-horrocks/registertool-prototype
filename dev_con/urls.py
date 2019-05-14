from django.urls import path
from . import views

app_name = "dev_con"

urlpatterns = [
    path("", views.pick_csv, name="pick_csv"),
    path("add_entry", views.add_entry, name="add_entry"),
    path("entry_complete", views.entry_complete, name="entry_complete")

]
