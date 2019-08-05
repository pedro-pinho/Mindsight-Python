from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics
from rest_framework.exceptions import ValidationError

from .models import Employees
from .serializers import EmployeeAPISerializer, EmployeeAPIIncludeSerializer, EmployeeAPIInfoSerializer

@api_view(['GET', 'POST'])
def api_employee(request):
    if request.method == 'GET':
        employees = Employees.objects.all()
        serializer = EmployeeAPISerializer(employees, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if (not request.data.get('name')):
            raise ValidationError('Nome do funcionário é obrigatório.')

        if (not request.data.get('salary')):
            raise ValidationError('Informe o salário.')

        duplicate = Employees.objects.filter(name=request.data.get('name')).first()
        if (duplicate):
            raise ValidationError('Nome já existe.')

        if (request.data.get('manager')):
            parent = Employees.objects.get(name=request.data.pop('manager'))
        else:
            parent = None
            
        from django.db import transaction
        with Employees.objects.disable_mptt_updates():
            serializer = EmployeeAPIIncludeSerializer(data=request.data, read_only=False)
            if serializer.is_valid():
                serializer.save(parent=parent)
                Employees.objects.rebuild()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeInfoList(generics.ListAPIView):
    serializer_class = EmployeeAPIInfoSerializer
    
    def get_queryset(self):
        name = self.kwargs['name'] or None
        boss = Employees.objects.filter(name=name) or None
        if (boss != None):
            return boss.first().descendants()
        return Employees.objects.all()