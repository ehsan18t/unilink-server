from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_department, name='create-department'),
    path('public/', department_list_public, name='department-list-public'),
    path('list/', department_list, name='department-list'),
    path('delete/', delete_department, name='delete-department'),
]
