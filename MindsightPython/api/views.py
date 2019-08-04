from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .forms import RegisterEmployeeForm
from .models import Employees
from .serializers import EmployeeAPISerializer, EmployeeAPIIncludeSerializer

@api_view(['GET', 'POST'])
def api_employee(request):
    if request.method == 'GET':
        employees = Employees.objects.all()
        serializer = EmployeeAPISerializer(employees, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        parent = Employees.objects.get(name=request.data.pop('manager'))
        serializer = EmployeeAPIIncludeSerializer(data=request.data, read_only=False)
        if serializer.is_valid():
            serializer.save(parent=parent)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)