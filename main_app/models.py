from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Clip(models.Model):
    title = models.CharField(max_length=300)
    html = models.TextField(max_length=10000, default='<div></div>')
    css = models.TextField(
        max_length=10000, default='border:4mm ridge rgba(211, 220, 50, .6);')
    difficulty = models.CharField(max_length=5, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    tags = models.ManyToManyField(Tag, related_name='clips')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_clips = models.ForeignKey(Clip, on_delete=models.CASCADE)
