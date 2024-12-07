from django.shortcuts import render

# Create your views here.
def PatientHomePage(request):
    return render(request, 'patientapp/PatientHomePage.html')
