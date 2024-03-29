from django import forms

from watcheck.common.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
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
