
from django.urls import path, re_path
from . import views

urlpatterns=[
    re_path(r'^search/$', views.search, name='search'),
    path('apply/<uuid:formcode>/', views.submitForm, name='apply'),
    path('apply/', views.submitForm, name='apply'),
    path('make-post', views.createPost, name='post'),
    path('make-form', views.createForm, name='form'),
    path('responses/<uuid:formcode>/', views.downloadResponse, name='download'),
    path('responses/', views.downloadResponse, name='download'),
]


