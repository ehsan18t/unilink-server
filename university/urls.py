from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_university, name='create-university'),
    path('pending/', pending_university_list, name='pending-university-list'),
    path('approved/', approved_university_list, name='approved-university-list'),
    path('list/', approved_university_list_public, name='approved-university-list-public'),
    path('approve/', approve_university, name='approve-university'),
    path('disapprove/', disapprove_university, name='disapprove-university'),
    path('ban/', ban_university, name='ban-university'),
    path('unban/', unban_university, name='unban-university'),
]
