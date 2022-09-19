from curses.ascii import EM
from django.shortcuts import render
from django.views.generic import (
    ListView, 
)

from .models import Employee


class ListAllEmployees(ListView):
    template_name = 'employees/list_all_employees.html'
    model = Employee
    context_object_name = 'employees'