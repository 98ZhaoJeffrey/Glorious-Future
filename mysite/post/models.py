from django.db import models
from django.db import models
from uuid import uuid4
from datetime import datetime
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
# Create your models here.

class TaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    pass

class Post(models.Model):
    UUID = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=100, blank=False)
    value = models.IntegerField(blank=False)
    dueDate = models.DateTimeField(blank=False)
    photo = models.ImageField(upload_to='thumbnails', blank=True, default='thumbnails/post.png')
    description = models.CharField(max_length=500)
    organization = models.ForeignKey('userApp.User', on_delete=models.CASCADE)
    tags = TaggableManager(through=TaggedItem, blank=True)
    link = models.URLField(default='https://www.google.com/',blank=True)
    def __str__(self):
        return self.title

"""
class Form(models.Model):
    UUID = models.OneToOneField('Post', on_delete=models.CASCADE, primary_key=True)
    question1 = models.CharField(max_length=400)
    question2 = models.CharField(max_length=400)
    question3 = models.CharField(max_length=400)


class Response(models.Model):
    responseID = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    form = models.ForeignKey('Form', on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=1000)
    answer2 = models.CharField(max_length=1000)
    answer3 = models.CharField(max_length=1000)
"""