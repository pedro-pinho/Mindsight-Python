from .models import Employees
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from rest_framework.validators import UniqueValidator

class EmployeeListSerializer(serializers.Serializer):
    name = serializers.CharField()
    salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    children = RecursiveField(required=False, allow_null=True, many=True)
    
    class Meta:
        model = Employees
        fields = ('name', 'salary','children',)

class EmployeeAPISerializer(serializers.Serializer):
    name = serializers.CharField()
    salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    manager = serializers.CharField()

    class Meta:
        model = Employees
        fields = ('name', 'salary','manager')

class EmployeeAPIIncludeSerializer(serializers.Serializer):
    name = serializers.CharField(validators=[UniqueValidator(queryset=Employees.objects.all())])
    salary = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        return Employees.objects.create(**validated_data)

    def save(self, *args, **kwargs):
        name = self.validated_data['name']
        salary = self.validated_data['salary']
        parent = kwargs['parent']
        
        new_node = Employees(name=name, salary=salary, parent=parent)
        new_node.insert_at(parent, position='last-child', save=True)
    class Meta:
        fields = ('id', 'name', 'salary','parent')
        extra_kwargs = {'name': {'error_messages': {'required': 'Nome do funcionário é obrigatório.'}}, 'salary': {'error_messages':{'required': 'Informe o salário.'}}}


class EmployeeAPIInfoSerializer(serializers.Serializer):
    name = serializers.CharField()
    salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        fields = ('name', 'salary')