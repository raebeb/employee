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

class ListEmployeesByArea(ListView):
    def get_queryset(self):
        area = self.kwargs['area']
        queryset = Employee.objects.filter(
            department__short_name=area
        )
        return queryset

    template_name = 'employees/list_by_area.html'

class ListEmployeesByKeyword(ListView):
    template_name = 'employees/list_by_keyword.html'
    context_object_name = 'employees'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword', '')
        queryset = Employee.objects.filter(first_name=keyword)
        print(queryset)
        return queryset