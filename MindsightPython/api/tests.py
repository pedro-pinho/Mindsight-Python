from __future__ import unicode_literals

from django.test import TestCase
from django.test.client import Client
from rest_framework.exceptions import ValidationError, ParseError

from MindsightPython.api.models import Employees
from .serializers import EmployeeAPISerializer, EmployeeAPIInfoSerializer

class TestAPI(TestCase):
    def setUp(self):
        self.client = Client()
        parent = Employees.objects.create(name='Chefe', salary=10000)
        Employees.objects.create(name='Empregado', salary=1000, parent=parent)

    def test_get_all_home(self):
        response = self.client.get('/')
        employees = Employees.objects.all()
        serializerTest = EmployeeAPISerializer(employees, many=True)
        serializerGet = EmployeeAPISerializer(response.context['employees'], many=True)
        self.assertEqual(serializerTest.data, serializerGet.data)
        self.assertEqual(response.status_code, 200)

    def test_response_code_ok_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_response_code_bad_url(self):
        response = self.client.get('/employeee')
        self.assertEqual(response.status_code, 404)

    def test_response_code_ok_post_boss(self):
        response = self.client.post('/', {'name':'CEO', 'salary': 500, 'Manager':None })
        self.assertEqual(response.status_code, 200)

    def test_response_code_ok_info_boss(self):
        response = self.client.get('/employees/Chefe')
        self.assertEqual(response.status_code, 200)

    def test_get_ok_info_boss(self):
        response = self.client.get('/employees/Chefe')
        employee = Employees.objects.filter(name='Empregado')

        serializerTest = EmployeeAPIInfoSerializer(employee, many=True)
        serializerGet = EmployeeAPIInfoSerializer(response.json(), many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializerTest.data, serializerGet.data)

    def test_response_code_bad_info_boss(self):
        response = self.client.get('/employees/!]][2')
        self.assertEqual(response.status_code, 404)

    def test_response_code_ok_post_sub(self):
        response = self.client.post('/', {'name':'Test test', 'salary': 11500, 'Manager':'Chefe' })
        self.assertEqual(response.status_code, 200)

    def test_bad_post_no_name(self):
        self.client.post('/', { "salary": 10.00,"manager": "Chefe"})
        self.assertRaises(ValidationError)

    def test_bad_post_no_salary(self):
        response = self.client.post('/', {'name':'Test test of test', 'Manager':'Chefe' })
        self.assertRaises(ValidationError)

    def test_response_code_ok_post_no_manager(self):
        response = self.client.post('/', {'name':'Test of test', 'salary': 120 })
        self.assertEqual(response.status_code, 200)

    def test_response_code_ok_post_float_salary(self):
        response = self.client.post('/', {'name':'Test jr test', 'salary': 120.51 })
        self.assertEqual(response.status_code, 200)

    def test_error_post_huge_salary(self):
        response = self.client.post('/', {'name':'Test test tested', 'salary': 12025658565.51, 'Manager':'Chefe' })
        self.assertRaises(ValidationError)

    def test_error_post_huge_name(self):
        response = self.client.post('/', {'name':'Test testtest test really long test test huge test test', 'salary': 120.51, 'Manager':'Chefe' })
        self.assertRaises(ValidationError)

    def test_error_post_invalid_salary(self):
        response = self.client.post('/', {'name':'Test 3 test', 'salary': 'abacaxi', 'Manager':'Chefe' })
        self.assertRaises(ValidationError)

    def test_error_post_invalid_name(self):
        response = self.client.post('/', {'name':12, 'salary': 1200, 'Manager':'Chefe' })
        self.assertRaises(ValidationError)

    def test_error_post_invalid_manager(self):
        response = self.client.post('/', {'name':'Jr Tests of tests', 'salary': 1200, 'Manager':14 })
        self.assertRaises(ValidationError)

    def test_bad_post_duplicate_name(self):
        response = self.client.post('/', { 'name':'Chefe', 'salary': 10.00,'manager': 'Chefe'})
        self.assertRaises(ValidationError)

class TestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        parent=Employees.objects.create(name='Chefe', salary=10000)
        Employees.objects.create(name='Funcionario', salary=1000, parent=parent)
    
    def test_name_label(self):
        employee = Employees.objects.get(id=1)
        field_label = employee._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Name')

    def test_salary_label(self):
        employee = Employees.objects.get(id=1)
        field_label = employee._meta.get_field('salary').verbose_name
        self.assertEquals(field_label, 'Salary')

    def test_parent_label(self):
        employee = Employees.objects.get(id=1)
        field_label = employee._meta.get_field('parent').verbose_name
        self.assertEquals(field_label, 'parent')
    
    def test_object_name_is_name(self):
        employee = Employees.objects.get(id=1)
        expected_object_name = f'{employee.name}'
        self.assertEquals(expected_object_name, str(employee))
    
    def test_descendants_count(self):
        employee = Employees.objects.get(id=1)
        self.assertEquals(1, employee.descendants().count())

    def test_manager_name(self):
        employee = Employees.objects.get(id=2)
        self.assertEquals('Chefe', employee.manager())

    def test_no_manager_name(self):
        employee = Employees.objects.get(id=1)
        self.assertEquals(None, employee.manager())

    def test_descendants_salary(self):
        employee = Employees.objects.get(id=1)
        self.assertEquals(1000, employee.descendants_salary())