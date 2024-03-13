from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Account(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(unique=True, max_length=30)
    last_name = models.CharField(unique=True, max_length=30)
    profile_picture = models.ImageField(blank=True, null=True, upload_to='images/')

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
