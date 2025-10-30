from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    
    path("", views.blog_home, name="blog_home"),
    path('<str:slug>', views.blog_post, name='blog_post'),
]