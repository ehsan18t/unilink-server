from django.urls import path
from .views import create_university, pending_university_list, approved_university_list, approved_university_list_public

urlpatterns = [
    path('create/', create_university, name='create-university'),
    path('pending/', pending_university_list, name='pending-university-list'),
    path('approved/', approved_university_list, name='approved-university-list'),
    path('list/', approved_university_list_public, name='approved-university-list-public'),
]
