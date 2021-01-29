from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify


class User(AbstractUser):
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.get_username()

    def can_view_post(self):
        """
        Checks if the user is a student or superuser

        Args:
        -----
        None

        Return:

        boolean: (True if student or superuser, false is organization)

        """
        
        #only students and admins may use the search, submitForm functions
        #organizations are considered staff but not super users
        return (not bool(self.is_staff) or self.is_superuser)

