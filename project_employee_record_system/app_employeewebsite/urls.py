from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.employee_index, name='emp-index'),
    path('employee/show/', views.employee_show, name='emp-show'),
    path('employee/edit/', views.employee_edit, name='emp-edit'),
    path('employee/add/', views.employee_add, name='emp-add'),
]