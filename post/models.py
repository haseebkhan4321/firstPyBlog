from django.db import models

from category.models import Category
from tag.models import Tag
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(default="default.jpg")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, )
    tag = models.ManyToManyField(Tag)
    total_views = models.IntegerField(default=0)
    flag_1 = models.BooleanField(default=False)  # flag for editor choice
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def feature_image(self):
        return self.postmedia_set.filter(featured=True).first()

    def __str__(self):
        return self.title
