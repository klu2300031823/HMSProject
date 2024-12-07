from django.urls import path, include
from . import views
app_name='patientapp'
urlpatterns=[
path('PatientHomePage/', views.PatientHomePage, name='PatientHomePage'),
]