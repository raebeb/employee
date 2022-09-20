from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('list-all-employee/', views.ListAllEmployees.as_view()),
    path('list-employee-by-area/<area>/', views.ListEmployeesByArea.as_view()),
    path('search_employee/', views.ListEmployeesByKeyword.as_view()),


]