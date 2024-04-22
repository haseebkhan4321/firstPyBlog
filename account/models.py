from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Account(models.Model):
    def __str__(self):
        return self.user.first_name +' '+ self.user.last_name

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(null=True)