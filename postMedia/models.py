from django.db import models

from post.models import Post


# Create your models here.
class PostMedia(models.Model):
    file = models.FileField(default='default.jpg')
    featured = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


