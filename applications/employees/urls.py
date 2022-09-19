from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('list-all-employee/', views.ListAllEmployees.as_view())
]