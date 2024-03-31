from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django import forms

from watcheck.accounts.models import Account, Address


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('username', 'email')
        widgets = {
            'email': forms.TextInput(
                attrs={'class': 'email-sign-in-input'}
            ),
            'username': forms.TextInput(
                attrs={'class': 'email-sign-in-input'}
            )
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus', None)

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'password-sign-in-input'
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'password-sign-in-input'
            }
        )
    )


class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Please enter a correct %(username)s and password."
    }

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'class': 'email-sign-in-input'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'password-sign-in-input'
            }
        )
    )


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['first_name', 'last_name', 'address', 'town', 'postcode', 'phone', 'email']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'first-name'}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'first-name'}
            ),
            'address': forms.TextInput(
                attrs={'class': 'address-input'}
            ),
            'town': forms.TextInput(
                attrs={'class': 'first-name'}
            ),
            'postcode': forms.TextInput(
                attrs={'class': 'first-name'}
            ),
            'phone': forms.TextInput(
                attrs={'class': 'first-name'}
            ),
            'email': forms.TextInput(
                attrs={'class': 'first-name'}
            ),

        }


class EditAddressForm(AddressForm):
    pass


class EditAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'username', 'email')

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'first-name'}),
            'last_name': forms.TextInput(
                attrs={'class': 'first-name'}),
            'username': forms.TextInput(
                attrs={'class': 'username'}),
            'email': forms.TextInput(
                attrs={'class': 'email'})
        }


class ChangePassword(PasswordChangeForm):
    class Meta:
        model = Account

    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'password'}
        )
    )

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'password'}
        )
    )

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'password'}
        )
    )
