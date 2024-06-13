from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', excel_index, name="excel_index"),



]
