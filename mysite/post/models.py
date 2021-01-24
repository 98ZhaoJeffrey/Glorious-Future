from django.db import models
from django.db import models
from uuid import uuid4
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
# Create your models here.

class TaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    pass

class Post(models.Model):
    UUID = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=100, blank=False)
    value = models.IntegerField(blank=False)
    dueDate = models.DateTimeField()
    photo = models.ImageField()
    description = models.CharField(max_length=500)
    organization = models.ForeignKey('userApp.User', on_delete=models.CASCADE)
    tags = TaggableManager(through=TaggedItem)
    
    def __str__(self):
        return self.title
"""
class Form(models.Model):
    Post = models.ForeignKey('Post', on_delete=models.CASCADE)
    Question1 = models.CharField(max_length=400)
    Question2 = models.CharField(max_length=400)
    Question3 = models.CharField(max_length=400)


class Response(models.Model):
    Form = models.ForeignKey('Form', on_delete=models.CASCADE)
    Answer1 = models.CharField(max_length=1000)
    Answer2 = models.CharField(max_length=1000)
    Answer3 = models.CharField(max_length=1000)
"""