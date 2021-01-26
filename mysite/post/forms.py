from django import forms
from django.forms import widgets
from .models import Post
from datetime import datetime
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):     
    title = forms.CharField(max_length=100, required=True, label='Title of Scholarship Post')
    description = forms.CharField(max_length=500, label='Description (Max 500 Char)', widget=forms.Textarea)
    value = forms.CharField(max_length=9, required=True, label='Value of the scholarship', widget=forms.widgets.NumberInput())
    dueDate = forms.DateTimeField(label='Deadline of the scholarship', required=True, widget=forms.widgets.DateInput(attrs={'type': 'datetime-local', 'format':'%m/%d/%Y %H:%M'}))
    photo = forms.ImageField(label='Image for the scholarship', required=False, widget=forms.widgets.FileInput(attrs={'class':'form-control', 'accept':'image/*'}))   

    class Meta:
        model = Post
        fields = ['title', 'description', 'value', 'dueDate', 'photo']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PostForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = self.cleaned_data
        dueDate = cleaned_data.get('dueDate')
        value = cleaned_data.get('value')
        print(dueDate < datetime.now(dueDate.tzinfo))
        if dueDate < datetime.now(dueDate.tzinfo):
            raise ValidationError(('Invalid date - renewal in past'))
        if int(value) < 0:
            raise ValidationError(('Scholarships must be above $0'))
        print(f"Data: {cleaned_data}")
        return cleaned_data

    def save(self, commit=True):
        post_instance = super(PostForm, self).save(commit=False)
        post_instance.organization_id = self.user.id
        if commit:            
            post_instance.save()

