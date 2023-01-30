from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('clips/', views.AllClips.as_view(), name="all_clips"),
    path('clips/new', views.ClipCreate.as_view(), name="clip_create"),
]
