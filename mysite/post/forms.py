from django import forms
from django.forms import widgets
from .models import Post, Form
from datetime import datetime
from django.core.exceptions import ValidationError
from taggit.forms import *

class PostForm(forms.ModelForm):     
    title = forms.CharField(max_length=100, required=True, label='Title of Scholarship Post')
    description = forms.CharField(max_length=500, required=False, label='Description (Max 500 Char)', widget=forms.Textarea)
    value = forms.CharField(max_length=9, required=True, label='Value of the scholarship', widget=forms.widgets.NumberInput())
    dueDate = forms.DateTimeField(label='Deadline of the scholarship', required=True, widget=forms.widgets.DateInput(attrs={'type': 'datetime-local', 'format':'%m/%d/%Y %H:%M'}))
    photo = forms.ImageField(label='Image for the scholarship', required=False, widget=forms.widgets.FileInput(attrs={'class':'form-control', 'accept':'image/*'}))   
    link = forms.URLField(label="Link to the questions form. Don't have one? Make one on our website!", required=True)
    tags = TagField(label="Tags for your post", help_text="Please put list them with one space in between each tag. Only the following tags will be saved: Everyone, Black, Hispanic, Female, LGBT. Immigrants, Disabled, and Poor")

    class Meta:
        model = Post
        fields = ['title', 'description', 'value', 'dueDate', 'photo', 'link']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PostForm, self).__init__(*args, **kwargs)

    def clean(self):
        """ Clean the data that we are given before we create the object
        Args
        -----
        None

        Returns
        -----
        dict: cleaned_data (Data that we can use to create an object with after checking for good inputs)

        """
        

        cleaned_data = self.cleaned_data
        dueDate = cleaned_data.get('dueDate')
        value = cleaned_data.get('value')

        #Due data cannot be in the past
        if dueDate < datetime.now(dueDate.tzinfo):
            raise ValidationError(('Invalid date - renewal in past'))
        
        #scholarship value must be greater than 0
        if int(value) < 0:
            raise ValidationError(('Scholarships must be above $0'))
        return cleaned_data

    def save(self, commit=True):
        """ Clean the data that we are given before we create the object
        Args
        -----
        boolean: commit (Django's way of telling the ORM to save the object)

        Returns
        -----
        None
        """

        
        post_instance = super(PostForm, self).save(commit=False)
        post_instance.organization_id = self.user.id
        if commit:            
            post_instance.save()
            return(post_instance)

class QuestionFormForm(forms.ModelForm):
    question1 = forms.CharField(max_length=400, required=True, label='First question of the post(Max 400 Chars Question)', widget=forms.Textarea(attrs={'rows':'5'}))
    question2 = forms.CharField(max_length=400, required=False, label='Second question of the post (Max 400 Chars Question)', widget=forms.Textarea(attrs={'rows':'5'}))
    question3 = forms.CharField(max_length=400, required=False,label='Third question of the post (Max 400 Chars Question)', widget=forms.Textarea(attrs={'rows':'5'}))
    class Meta:
        model = Form
        fields = ['question1', 'question2', 'question3']
