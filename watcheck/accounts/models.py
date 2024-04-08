from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class Account(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Address(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    town = models.CharField(max_length=20)
    postcode = models.IntegerField()
    phone = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    email = models.EmailField(max_length=202)
    current_profile = models.ForeignKey(Account, on_delete=models.CASCADE)

