from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('list-all-employee/', views.ListAllEmployees.as_view()),
    path('list-employee-by-area/<area>/', views.ListEmployeesByArea.as_view()),
    path('search-employee/', views.ListEmployeesByKeyword.as_view()),
    path('list-employee-habilities/', views.ListEmployeeHabilities.as_view()),
    path('view-employee/<pk>/', views.EmployeeDetailView.as_view()),
    path('create-employee/', views.EmployeeCreateView.as_view()),





]