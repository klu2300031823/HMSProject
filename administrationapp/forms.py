from django import forms

from django import forms
from .models import PatientList


class PatientsForm(forms.ModelForm):
    class Meta:
        model = PatientList
        fields = ['Register_Number', 'Name', 'Date', 'Reason']






