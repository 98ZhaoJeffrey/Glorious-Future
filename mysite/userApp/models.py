from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify


class User(AbstractUser):
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.get_username()

    def can_view_post(self):
        #only students and admins may use the search, submitForm functions
        return (not bool(self.is_staff) or self.is_superuser)

