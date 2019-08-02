from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from .forms import RegisterEmployeeForm
from .models import Employees
from .serializers import EmployeeListSerializer

class registerView(View):
    model = Employees
    registerForm = RegisterEmployeeForm
    template_name = 'register.html'
    
    def get(self, request):
        employees = Employees.objects.root_nodes()
        form = self.registerForm()
        serializer = EmployeeListSerializer(employees, many=True)
        # return Response(serializer.data)
        return render(request, self.template_name, {'form': form, 'employees': employees})

    def post(self, request):
        form = self.registerForm(self.request.POST or None)
        # manager = get_object_or_404(Employees, name=manager_name)
        employees = Employees.objects.all()
        if form.is_valid():
            employee = form.save(commit=True)
            # employee.manager = manager
            # employee.save()
            employees = Employees.objects.all()
            form = self.registerForm()
            messages.success(request, 'Inserido com sucesso.')
        return render(request, self.template_name, {'form': form, 'employees': employees})

register = registerView.as_view()