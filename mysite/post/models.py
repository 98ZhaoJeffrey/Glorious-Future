from django.db import models

# Create your models here.

from django.db import models
from uuid import uuid4
from taggit.managers import TaggableManager
#from ..userApp.models import User

# Create your models here.

class Post(models.Model):
    UUID = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(max_length=100, blank=False)
    value = models.IntegerField(blank=False)
    dueDate = models.DateTimeField()
    photo = models.ImageField()
    description = models.CharField(max_length=500)
    organization = models.ForeignKey('userApp.User', on_delete=models.CASCADE)
    tags = TaggableManager()
    
    def __str__(self):
        return self.title

"""
Each post needs the org who made it is done
Title of the Post done
Date the post is due done
Link to the post
Desciption of the post
Photo for the post done
uuid of the post(primary key) done
tags for the post
"""