
from django.urls import path, re_path
from . import views

urlpatterns=[
    re_path(r'^search/$', views.search, name='search'),
    path('apply', views.submitForm, name='apply'),
    path('make-post', views.createPost, name='post'),
    path('make-form', views.createForm, name='form'),
]


