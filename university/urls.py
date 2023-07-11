from django.urls import path
from .views import create_university

urlpatterns = [
    path('api/universities/', create_university, name='create-university'),
]
