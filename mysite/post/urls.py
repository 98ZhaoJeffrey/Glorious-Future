
from django.urls import path, re_path
from . import views

urlpatterns=[
    re_path(r'^search/$', views.search, name='search'),
    path('make-post', views.createPost, name='post'),
    path('submit-form', views.submitForm, name='submit'),
]


