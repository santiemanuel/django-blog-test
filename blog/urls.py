from django.contrib import admin
from django.urls import path
from .views import posts, create_post

urlpatterns = [
    path("", posts, name="posts"),
    path("create_post/", create_post, name="create_post"),
]
