from django.urls import path, include
from . import views
app_name='staffapp'
urlpatterns=[
path('StaffHomePage/', views.StaffHomePage, name='StaffHomePage'),
]