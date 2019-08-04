from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from MindsightPython.api import views

app_name = 'api'
urlpatterns = [
    path('', views.api_employee, name='employees')
]
