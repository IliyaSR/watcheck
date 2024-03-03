from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms

from watcheck.account.models import Account


class RegisterForm(UserCreationForm):
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

