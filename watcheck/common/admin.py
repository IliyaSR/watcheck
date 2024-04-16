from django.contrib import admin

from watcheck.common.models import Order


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass