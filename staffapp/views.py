from django.shortcuts import render

# Create your views here.
def StaffHomePage(request):
    return render(request, 'staffapp/StaffHomePage.html')
