from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from MindsightPython.api.models import Employees
from MindsightPython.api.serializers import EmployeeListSerializer

def home(request):
    employees = Employees.objects.all()
    serializer_class = EmployeeListSerializer

    context = {
        'employees': employees
    }
    return render(request,'home.html', context)