from django.db import models
from university.models import University


class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

