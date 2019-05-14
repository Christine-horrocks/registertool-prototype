from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('createcsv.urls')),
    path('pick_csv', include('dev_con.urls')),
    path('admin/', admin.site.urls),
]
