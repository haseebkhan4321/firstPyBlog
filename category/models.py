from django.db import models


# Create your models here.
class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
