from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from unittest.mock import patch
from django.urls import reverse, resolve
from rest_framework.authtoken.models import Token
from django.test import SimpleTestCase
from university.views import *

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
            "doc_url" : "Test url",
            "code": 1,
            "name": "Test Uni",
            "domain": "uni",
            "admin": {
                "first_name": "mr",
                "last_name": "x",
                "username": "uniadmin",
                "email": "mdashik560@outlook.com"
            }
        }
    
    def test_create_university_url(self):
        self.assertEquals(resolve(self.url).func, create_university)
       
    def test_create_uni_with_no_data(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 400)
    
    def test_create_uni_with_data(self):
        response = self.client.post(self.url,self.create_uni_data,format="json")     
        self.assertEqual(response.status_code, 200)

class TestApproveUni(APITestCase):

    def setUp(self):
        self.url = reverse('approved-university-list-public')

    def test_approved_university_list_public_url(self):
        self.assertEquals(resolve(self.url).func, approved_university_list_public)

    def test_approve_university_list_public(self):
        response = self.client.get(self.url);
        self.assertEqual(response.status_code, 200)
