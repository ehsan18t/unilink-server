from django.test import SimpleTestCase
from django.urls import resolve, reverse
from university.views import *


class UniversityUrlsTests(SimpleTestCase):

    
    def test_pending_university_list_resolved(self):
        url = reverse('pending-university-list')
        self.assertEquals(resolve(url).func, pending_university_list)
    
    def test_approved_university_list_resolved(self):
        url = reverse('approved-university-list')
        self.assertEquals(resolve(url).func, approved_university_list)
    
    def test_approved_university_list_public_resolved(self):
        url = reverse('approved-university-list-public')
        self.assertEquals(resolve(url).func, approved_university_list_public)
    
    def test_approve_university_resolved(self):
        url = reverse('approve-university')
        self.assertEquals(resolve(url).func, approve_university)
    
    def test_disapprove_university_resolved(self):
        url = reverse('disapprove-university')
        self.assertEquals(resolve(url).func, disapprove_university)
    
    def test_ban_university_resolved(self):
        url = reverse('ban-university')
        self.assertEquals(resolve(url).func, ban_university)
    
    def test_unban_university_resolved(self):
        url = reverse('unban-university')
        self.assertEquals(resolve(url).func, unban_university)
    
    