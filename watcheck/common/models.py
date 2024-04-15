from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models

from watcheck.accounts.models import Address, Account
from watcheck.accounts.validators import only_letters_name, only_letters_town
from watcheck.watch.models import Watch


# Create your models here.
class Bag(models.Model):
    watch_image = models.ImageField(upload_to='images/')
    brand_watch = models.CharField(max_length=30)
    model_watch = models.CharField(max_length=60)
    price = models.IntegerField()
    watch_code = models.CharField(max_length=20)


class Order(models.Model):
    first_name = models.CharField(max_length=20, validators=[MinLengthValidator(2), only_letters_name])
    last_name = models.CharField(max_length=20, validators=[MinLengthValidator(2), only_letters_name])
    address = models.CharField(max_length=20)
    town = models.CharField(max_length=20, validators=[MinLengthValidator(2), only_letters_town])
    postcode = models.IntegerField()
    phone = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    email = models.EmailField(max_length=202)
    current_profile = models.ForeignKey(Account, on_delete=models.CASCADE)
    current_watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
