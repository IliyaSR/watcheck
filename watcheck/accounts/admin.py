from django.contrib import admin

from watcheck.accounts.models import Account


# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass