from django.db import models
from django.contrib import admin

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    body = models.TextField()
    timestamp = models.DateTimeField()

admin.register(BlogPost)