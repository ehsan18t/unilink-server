from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from unittest.mock import patch
from django.urls import reverse, resolve
from rest_framework.authtoken.models import Token
from django.test import SimpleTestCase
from university.views import create_university

from university.models import University 
from university.serializers import UniversitySerializer
from users.permissions import SiteAdminOnly
from users.models import UserAccount
from users.permissions import SiteAdminOnly
from users.models import UserType
import pdb

class TestCreateUni(APITestCase):
    def setUp(self):
        self.url = reverse('create-university')

        self.create_uni_data = {
            "name": "Test Uni",
            "domain": "uni",
            "admin": {
                "first_name": "mr",
                "last_name": "x",
                "username": "uniadmin",
                "email": "mdashik560@outlook.com"
            }
        }

       
    def test_create_uni_with_no_data(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 400)
    
    