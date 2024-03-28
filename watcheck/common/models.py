from django.core.validators import MaxValueValidator
from django.db import models

from watcheck.accounts.models import Address, Account


# Create your models here.
class Bag(models.Model):
    watch_image = models.ImageField(upload_to='images/')
    brand_watch = models.CharField(max_length=30)
    model_watch = models.CharField(max_length=60)
    price = models.IntegerField()


class Order(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    town = models.CharField(max_length=20)
    postcode = models.IntegerField()
    phone = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    email = models.EmailField(max_length=202)
    brand_watch = models.CharField(max_length=30)
    current_profile = models.ForeignKey(Account, on_delete=models.CASCADE)
