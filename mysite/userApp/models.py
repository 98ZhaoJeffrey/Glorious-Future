from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
import hashlib

    
# Create your models here.
class UserInfo(models.Model):
    """Parent class that has children Student and Organization"""

    username = models.CharField(primary_key=True, max_length = 32)
    email = models.EmailField(blank = False)
    password = models.CharField(max_length=32, blank = False)
    createdate = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(max_length=32, blank=True)

    def __str__(self):
        return self.username
    
    def slug(self):
        """Generates a human-friendly string used for the account's urls
        
        Parameters:
        
        None

        Returns:

        String: The username with hypens inbetween spaces
        """
        return slugify(self)
    
    def createHash(self):
        """Generates a hash used for reseting passwords

        Parameters:

        None

        Returns:

        String: A string of size 32 in hexadecimal

        """

        hashingString = str(self.password + self.email)
        return(hashlib.md5(hashingString.encode()).hexdigest())

    def save(self, *args, **kargs):
        """Saves the object to the database after setting the user's token
        
        Parameters:
        
        *args: Necessary argument to override the save function
        **kargs: Necessary argument to override the save function

        Returns:

        None
        
        """
        self.token = self.createHash()
        super(UserInfo, self).save(*args, **kargs)

    class Meta:
        abstract = True
class Student(UserInfo):
    firstName = models.CharField(max_length=32, blank = False)
    lastName = models.CharField(max_length=32, blank = False)
    school = models.CharField(max_length=32, blank = False)
    class Meta:
        db_table = 'Student'

class Organization(UserInfo):
    organizationName = models.CharField(max_length=32, blank = False)

    class Meta:
        db_table = 'Organization'