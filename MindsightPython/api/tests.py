from __future__ import unicode_literals

from django.test import TestCase
from django.test.client import Client
from rest_framework.exceptions import ValidationError

class TestAPI(TestCase):
    def setUp(self):
        self.client = Client()

    def test_ok(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_bad_url(self):
        response = self.client.get('/employeee')
        self.assertEqual(response.status_code, 404)

    def test_ok_post_boss(self):
        response = self.client.post('/', {'name':'Chefe', 'salary': 500, 'Manager':None })
        self.assertEqual(response.status_code, 200)

    def test_ok_post_sub(self):
        response = self.client.post('/', {'name':'FuncionarioTeste', 'salary': 11500, 'Manager':'Chefe' })
        self.assertEqual(response.status_code, 200)

    def test_bad_post_no_name(self):
        response = self.client.post('/', { 'salary': 10.00,'manager': 'Chefe'})
        self.assertRaises(ValidationError)

    def test_bad_post_no_salary(self):
        response = self.client.post('/', {'name':'FuncionarioTeste2', 'Manager':'Chefe' })
        self.assertRaises(ValidationError)

    def test_ok_post_no_manager(self):
        response = self.client.post('/', {'name':'FuncionarioTeste3', 'salary': 120 })
        self.assertEqual(response.status_code, 200)

    def test_ok_post_float_salary(self):
        response = self.client.post('/', {'name':'FuncionarioTeste3', 'salary': 120.51 })
        self.assertEqual(response.status_code, 200)

    def test_bad_post_huge_salary(self):
        response = self.client.post('/', {'name':'FuncionarioTeste2', 'salary': 12025658565.51, 'Manager':'Chefe' })
        self.assertRaises(ValidationError)

    def test_bad_post_huge_name(self):
        response = self.client.post('/', {'name':'FuncionarioTesteLikeALotHugeNameReallyBigIsThatPossible', 'salary': 120.51, 'Manager':'Chefe' })
        self.assertRaises(ValidationError)

    def test_bad_post_invalid_salary(self):
        response = self.client.post('/', {'name':'FuncionarioTeste3', 'salary': 'abacaxi', 'Manager':'Chefe' })
        self.assertRaises(ValidationError)

    def test_bad_post_invalid_name(self):
        response = self.client.post('/', {'name':12, 'salary': 1200, 'Manager':'Chefe' })
        self.assertRaises(ValidationError)

    def test_bad_post_invalid_manager(self):
        response = self.client.post('/', {'name':'FuncionarioTeste3', 'salary': 1200, 'Manager':14 })
        self.assertRaises(ValidationError)

from MindsightPython.api.models import Employees
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

    def test_descendants_salary(self):
        employee = Employees.objects.get(id=1)
        self.assertEquals(1000, employee.descendants_salary())