from django import forms
from .models import Employee

class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        # fields = ("full_name", "contact")
        model = Employee
