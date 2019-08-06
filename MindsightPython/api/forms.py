from django import forms
from .models import Employees

#Not currently in use
class RegisterEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ('name','parent','salary')

    def clean_name(self):
        name = self.cleaned_data['name']
        if Employees.objects.filter(name=name):
            raise forms.ValidationError('Já existe um funcionário com esse nome.')
        return name