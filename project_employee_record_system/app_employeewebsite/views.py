from django.shortcuts import render
from .forms import EmployeeCreateForm

# Create your views here.
def employee_index(request):
    return render(request, 'employees/index_employee.html')

def employee_add(request):
    emp_create_form = EmployeeCreateForm()
    context = {"form": emp_create_form}
    return render(request, 'employees/add_employee.html', context)

def employee_edit(request):
    return render(request, 'employees/edit_employee.html')

def employee_show(request):
    return render(request, 'employees/show_employee.html')