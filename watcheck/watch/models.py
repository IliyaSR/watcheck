from django.db import models


# Create your models here.
class Watch(models.Model):
    main_image = models.ImageField()
    image_for_shop_page = models.ImageField()
    first_small_image = models.ImageField()
    second_small_image = models.ImageField()
    third_small_image = models.ImageField()
    fourth_small_image = models.ImageField()
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    details_text = models.TextField()
    watch_code = models.CharField(max_length=20)
    price = models.IntegerField()
    case_material = models.CharField(max_length=30)
    strap_material = models.CharField(max_length=30)
    movement = models.CharField(max_length=30)
    water_resistance = models.IntegerField()
    case_diameter = models.FloatField()
    case_thickness = models.FloatField()
    glass = models.CharField(max_length=30)

    def __str__(self):
        return self.brand