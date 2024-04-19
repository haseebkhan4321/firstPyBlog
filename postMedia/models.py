from django.db import models

from post.models import Post


# Create your models here.
class PostMedia(models.Model):
    def __str__(self):
        return self.file.url
    file = models.FileField(default='default.jpg')
    featured = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
