from django.contrib import admin
from django.urls import path
from MindsightPython.api import views

app_name = 'api'
urlpatterns = [
    path('', views.api_employee, name='employees'),
    path('<name>', views.EmployeeInfoList.as_view(), name='employees_info')
]
