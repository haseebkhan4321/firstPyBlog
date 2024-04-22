from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug or self.name != self.slug:
            self.slug = self.generate_unique_slug(self.name)
        super().save(*args, **kwargs)

    def generate_unique_slug(self, name):
        slug = slugify(name)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exclude(id=self.id).exists():
            unique_slug = f"{slug}-{num}"
            num += 1
        return unique_slug
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
