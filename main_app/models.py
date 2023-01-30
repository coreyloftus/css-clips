from django.db import models

# Create your models here.


class Clip(models.Model):
    title = models.CharField(max_length=300)
    body = models.CharField(max_length=10000)
    difficulty = models.CharField(max_length=5, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
