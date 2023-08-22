from django.db import models
from enum import Enum


class CourseType(Enum):
    THEORY = '1'
    LAB = '2'

    @classmethod
    def choices(cls):
        return [(key.value, key.value) for key in cls]


class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    type = models.IntegerField(choices=CourseType.choices(), default=CourseType.THEORY.value)
    university = models.ForeignKey('university.University', on_delete=models.CASCADE, related_name='university')

    def __str__(self):
        return f'{self.code} {self.name}'


class Section(models.Model):
    name = models.CharField(max_length=5)
    trimester = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    students = models.ManyToManyField('users.UserAccount', related_name='students')
    faculty = models.ManyToManyField('users.UserAccount', related_name='sections_faculty')

    def __str__(self):
        return f'{self.trimester} {self.name}'

