from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('clips/', views.AllClips.as_view(), name="all_clips"),
]
