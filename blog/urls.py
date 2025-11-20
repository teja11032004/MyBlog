from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path("", views.blog_home, name="blog_home"),  
    path("<str:slug>/", views.blog_post, name="blog_post"),
    path("<str:slug>/add-comment/", views.add_comment, name="add_comment"),
    path("reply/<int:comment_id>/", views.post_reply, name="post_reply"),

]
