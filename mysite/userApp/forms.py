from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name', required=False)
    location = forms.CharField(label='Location of the organization', required=False)
    is_staff = forms.BooleanField(label='I am an Organization', required=False)

    def save(self, commit=True):
        user_instance = super(UserRegisterForm, self).save(commit=False)
        if commit:            
            user_instance.save()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', "location", "is_staff"]