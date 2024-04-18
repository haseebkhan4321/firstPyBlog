from django.db import models

from category.models import Category
from comment.models import Comment
from tag.models import Tag
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    author_name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(default="default.jpg")
    category = models.OneToOneField(
        Category,
        on_delete=models.CASCADE,
    )
    author = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    tag = models.ManyToManyField(Tag)
    comment = models.ManyToManyField(Comment)
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
