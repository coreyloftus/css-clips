from django.db import models

# Create your models here.


class Clip(models.Model):
    title = models.CharField(max_length=300)
    html = models.TextField(max_length=10000, default='<div></div>')
    css = models.TextField(
        max_length=10000, default='border:4mm ridge rgba(211, 220, 50, .6);')
    difficulty = models.CharField(max_length=5, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
