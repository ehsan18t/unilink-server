from django.urls import path
from .views import *

urlpatterns = [
    path('', get_courses, name='get_courses'),
    path('create/', create_course, name='create_course'),
    path('delete/', delete_course, name='delete_course'),
    path('section/', get_section, name='get_section'),
    path('sections/', get_course_sections, name='get_course_sections'),
    path('section/create/', create_section, name='create_section'),
    path('section/update/', update_section, name='create_section'),
    path('section/delete/', delete_section, name='delete_section'),
    path('section/add-faculty/', add_faculty_to_section, name='add_faculty_to_section'),
    path('section/remove-student/', remove_student_from_section, name='remove_student_from_section'),
    path('section/remove-user/', remove_user_from_section, name='remove_user_from_section'),
]
