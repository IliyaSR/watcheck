from django.contrib import admin

from django.contrib.auth import admin as auth_admin

from watcheck.accounts.forms import RegisterForm
from watcheck.accounts.models import Account, Address


# Register your models here.
@admin.register(Account)
class AccountAdmin(auth_admin.UserAdmin):
    model = Account
    add_form = RegisterForm

    list_display = ('pk', 'username', 'is_staff', 'is_superuser')
    search_fields = ['username']
    ordering = ['pk']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username',)}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", 'email', "password1", "password2", 'is_staff'),
            },
        ),
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    model = Account
    list_display = ('email', 'phone')
