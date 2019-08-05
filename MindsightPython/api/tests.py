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