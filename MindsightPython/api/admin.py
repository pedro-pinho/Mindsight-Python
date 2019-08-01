from django.contrib import admin

from .models import Employees

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['name','salary','parent']
    search_fields = ['name','salary','parent']
admin.site.register(Employees, EmployeesAdmin)