from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Account(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(unique=True, max_length=30)


