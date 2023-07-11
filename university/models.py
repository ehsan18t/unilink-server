from django.db import models


class University(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'


class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
