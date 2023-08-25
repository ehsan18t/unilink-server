from django.urls import path
from .views import *

urlpatterns = [
    path('', get_chat_list, name='get-chat-list'),
    path('get-chat/', get_chat, name='get-chat'),
]
