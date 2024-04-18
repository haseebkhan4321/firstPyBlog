from django.db import models


# Create your models here.
class Comment(models.Model):
    class Status(models.TextChoices):
        ACCEPTED = "accepted"
        REJECTED = "rejected"
        PENDING = "pending"

    content = models.CharField(max_length=255)
    status = models.CharField(
        max_length=8,
        choices=Status,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
