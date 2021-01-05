from django import urls
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
     path('signup', views.signup, name='signup'),
     path('login', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
     path('logout', auth_views.LogoutView.as_view(), name='logout'),
     path('profile', views.profile, name='profile')
]
#template_name='logout.html')