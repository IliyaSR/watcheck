from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models
from django_countries.fields import CountryField

from watcheck.accounts.validators import only_letters_name, only_letters_town


# Create your models here.
class Account(AbstractUser):
    email = models.EmailField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30, blank=True, null=True,
                                  validators=[MinLengthValidator(2), only_letters_name])
    last_name = models.CharField(max_length=30, blank=True, null=True,
                                 validators=[MinLengthValidator(2), only_letters_name])
    account_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Address(models.Model):
    first_name = models.CharField(max_length=20, validators=[MinLengthValidator(2), only_letters_name])
    last_name = models.CharField(max_length=20, validators=[MinLengthValidator(2), only_letters_name])
    address = models.CharField(max_length=20, validators=[MinLengthValidator(5)])
    town = models.CharField(max_length=20, validators=[MinLengthValidator(2), only_letters_town])
    postcode = models.IntegerField()
    phone = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    email = models.EmailField(max_length=20)
    current_profile = models.ForeignKey(Account, on_delete=models.CASCADE)
