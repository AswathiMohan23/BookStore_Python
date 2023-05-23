from django.urls import reverse
from rest_framework.test import APITestCase, APIClient


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.book_url = reverse('book')
        self.jwt_token_url = reverse('token_obtain_pair')
        self.client = APIClient()
        self.admin_user_data = {
            "username": "aswathi",
            "password": "aswathi",
            "first_name": "aswathi",
            "last_name": "aswathi",
            "email": "aswathi@gmail.com",
            "is_superuser":True
        }
        self.normal_user_data = {
            "username": "harry",
            "password": "harry",
            "first_name": "harry",
            "last_name": "potter",
            "email": "harry@gmail.com",
            "location": "kochi",
            "is_superuser": False
        }

        self.invalid_data = {
            "username": "",
            "password": "",
            "first_name": "",
            "last_name": "",
            "email": "",
            "location": ""
        }
        self.valid_user = {
            "username": "harry",
            "password": "harry"
        }
        self.invalid_empty_field = {
            "username": "",
            "password": "harry",
            "first_name": "harry",
            "last_name": "potter",
            "email": "harry@gmail.com",
            "location": "kochi"

        }
        self.invalid_login_field = {
            "username": "",
            "password": ""
        }
        self.empty_login_field = {
            "username": "harry",
            "password": ""
        }

        self.wrong_login = {
            "username": "harry",
            "password": "abc"
        }
        self.valid_login = {
            "username": "harry",
            "password": "harry"
        }
        self.valid_book = {
            "book_name": "abc",
            "description": "xyz",
            "author": "qqq",
            "price": 1020,
            "quantity": 2
        }
        self.invalid_book = {
            "book_name": "",
            "description": "pqr",
            "author": "aaa",
            "price": 1020,
            "quantity": 2
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def get_normal_user_token(self):
        self.client.post(self.register_url, data=self.normal_user_data)
        self.login_data = {'username': 'harry', 'password': 'harry'}
        response = self.client.post(self.jwt_token_url, self.login_data, format='json')
        self.assertEqual(response.status_code, 200)
        return response.data['access']

    def get_admin_token(self):
        value=self.client.post(self.register_url, data=self.admin_user_data)
        print(value.data)
        self.login_data = {'username': 'aswathi', 'password': 'aswathi'}
        response = self.client.post(self.jwt_token_url, self.login_data, format='json')
        self.assertEqual(response.status_code, 200)
        return response.data['access']
