from django.db import models

from post.models import Post


# Create your models here.

class Review(models.Model):

    def __str__(self):
        return self.content

    class Status(models.TextChoices):
        ACCEPTED = "accepted"
        REJECTED = "rejected"
        PENDING = "pending"

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255,default='anonymous')
    email = models.EmailField(null=True)
    content = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    status = models.CharField(
        max_length=8,
        choices=Status,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
