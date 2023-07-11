from django.urls import path
from .views import create_university

urlpatterns = [
    path('create/', create_university, name='create-university'),
]
