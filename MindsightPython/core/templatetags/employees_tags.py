from django import template
from MindsightPython.api.models import Employees
register = template.Library()

@register.simple_tag
def get_child_employees_tag(employee):
    return Employees.get_child_employees(employee)
