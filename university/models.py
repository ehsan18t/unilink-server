from django.db import models
from users.models import UserAccount


class Settings(models.Model):
    email_pattern = models.CharField(max_length=100)  # university pattern
    sid_pattern = models.CharField(max_length=100)  # student id pattern
    is_registration_enabled = models.BooleanField(default=False)


class University(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=300)
    settings = models.ForeignKey(Settings, on_delete=models.DO_NOTHING, null=True, blank=True)
    admin = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING, related_name='university_admin')
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'
