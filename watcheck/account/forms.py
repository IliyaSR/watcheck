from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from watcheck.account.models import Account


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('username', 'email', 'first_name')
        widgets = {
            'email': forms.TextInput(
                attrs={'class': 'email-sign-in-input'}
            ),
            'username': forms.TextInput(
                attrs={'class': 'email-sign-in-input'}
            ),
            'first_name': forms.TextInput(
                attrs={'class': 'email-sign-in-input'}
            )
        }

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
    class Meta(AuthenticationForm):
        widgets = {
            'email': forms.TextInput(
                attrs={'class': 'email-sign-in-input'}
            )
        }

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'password-sign-in-input'
            }
        )
    )
