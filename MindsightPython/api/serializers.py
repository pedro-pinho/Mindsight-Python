from .models import Employees
from rest_framework import routers, serializers, viewsets
from rest_framework_recursive.fields import RecursiveField

class EmployeeListSerializer(serializers.Serializer):
    name = serializers.CharField()
    salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    # children = serializers.ListField(child=RecursiveField())
    children = RecursiveField(required=False, allow_null=True, many=True)
    # parent = serializers.SerializerMethodField()
 
    class Meta:
        model = Employees
        fields = ('id','name', 'salary','children',)
        
    # def get_parent(self, obj):
    #     parent = Employees.objects.filter(parent=obj.id)
    #     if parent is not None:
    #         return EmployeeListSerializer(parent, many=True, context=self.context).data
    #     else:
    #         return None



            

    # def create(self, validated_data):
    #     return Employees(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.salary = validated_data.get('salary', instance.content)
    #     instance.manager = validated_data.get('manager', instance.created)
    #     return instance