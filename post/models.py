from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    author_name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(default="default.jpg")
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
