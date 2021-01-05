from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify


class User(AbstractUser):
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.get_username()

