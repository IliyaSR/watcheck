from django.contrib import admin

from watcheck.accounts.models import Account, Address


# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass