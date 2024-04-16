from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from watcheck.accounts.models import Account
from watcheck.common.validators import only_capital_letters


# Create your models here.
class Watch(models.Model):
    specific_brands = (
        ('ARNOLD & SON', "ARNOLD & SON"),
        ('FESTINA', 'FESTINA'),
        ('LIGE', 'LIGE'),
        ('MVMT', 'MVMT'),
        ('FOSSIL', 'FOSSIL')
    )

    main_image = models.ImageField(upload_to='images/')
    image_for_shop_page = models.ImageField(upload_to='images/')
    first_small_image = models.ImageField(upload_to='images/')
    second_small_image = models.ImageField(upload_to='images/')
    third_small_image = models.ImageField(upload_to='images/', blank=True, null=True)
    fourth_small_image = models.ImageField(upload_to='images/', blank=True, null=True)
    brand = models.CharField(max_length=30, validators=(only_capital_letters,), choices=specific_brands)
    model = models.CharField(max_length=30)
    details_text = models.TextField()
    watch_code = models.CharField(max_length=20, validators=(only_capital_letters,))
    price = models.IntegerField()
    case_material = models.CharField(max_length=30)
    strap_material = models.CharField(max_length=30)
    movement = models.CharField(max_length=30)
    water_resistance = models.IntegerField()
    case_diameter = models.IntegerField()
    case_thickness = models.FloatField()
    glass = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Watch'
        verbose_name_plural = 'Watches'

    def __str__(self):
        return self.brand


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    text_review = models.TextField(max_length=120)
    date_post = models.DateField(auto_now_add=True)
    person_review = models.ForeignKey(Account, on_delete=models.CASCADE)
    rated_watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
