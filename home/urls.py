from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("learn", views.learn, name="learn"),
    path("teach", views.teach, name="teach"),
    path("projects", views.projects, name="projects"),
    path("about", views.about, name="about"),
]