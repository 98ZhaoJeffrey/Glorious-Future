from django.db import models
from django.db import models
from uuid import uuid4
from datetime import datetime
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
from django.core.validators import MinValueValidator
# Create your models here.

class TaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    pass

class Post(models.Model):
    UUID = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=100, blank=False)
    value = models.PositiveIntegerField(blank=False, validators=[MinValueValidator(1)])
    dueDate = models.DateTimeField(blank=False)
    photo = models.ImageField(upload_to='thumbnails', blank=True, default='thumbnails/post.png')
    description = models.CharField(max_length=500)
    organization = models.ForeignKey('userApp.User', on_delete=models.CASCADE)
    tags = TaggableManager(through=TaggedItem, blank=True)
    link = models.URLField()
    
    def __str__(self):
        """Return the title of the post """
        return self.title


class Form(models.Model):
    UUID = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    question1 = models.CharField(max_length=400)
    question2 = models.CharField(max_length=400, blank=True)
    question3 = models.CharField(max_length=400, blank=True)
    
class Response(models.Model):
    responseID = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    form = models.ForeignKey('Form', on_delete=models.CASCADE)
    user = models.ForeignKey('userApp.User', on_delete=models.CASCADE)
    submitDate = models.DateTimeField(auto_now_add=True)
    answer1 = models.CharField(max_length=1000)
    answer2 = models.CharField(max_length=1000,blank=True)
    answer3 = models.CharField(max_length=1000,blank=True)
