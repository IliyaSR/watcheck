from django.db import models


# Create your models here.
class Bag(models.Model):
    watch_image = models.ImageField(upload_to='images/')
    brand_watch = models.CharField(max_length=30)
    model_watch = models.CharField(max_length=60)
    price = models.IntegerField()
