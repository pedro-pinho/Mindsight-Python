from django import forms
from .models import Employees


class RegisterEmployeeForm(forms.ModelForm):
    # name = forms.CharField(label='Nome', max_length=50)
    # manager = forms.CharField(label='Gerente', max_length=50)
    # salary = forms.forms.DecimalField(label='Salário', max_digits=10, decimal_places=2)
    class Meta:
        model = Employees
        fields = ('name','parent','salary')

    def clean_name(self):
        name = self.cleaned_data['name']
        if Employees.objects.filter(name=name):
            raise forms.ValidationError('Já existe um funcionário com esse nome.')
        return name

    # def save(request, manager_name):
    #     form = registerForm(request.POST or None)
    #     parent = get_object_or_404(Employees, name=manager_name)
    #     if form.is_valid():
    #         employee = form.save(commit=False)
    #         employee.manager = manager
    #         employee.save()
    #         form = registerForm()
    #     return redirect('core:home')