from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('', views.profile, name='profile'),
    path('profile/pass_change/', views.pass_change, name='pass_change'),
    path('resume/', views.resume, name = 'resume')
]
