from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Имя',
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Фамилия',
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Эл. почта',
            }
        )
    )

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Адресс',
            }
        )
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Телефон',
            }
        )
    )

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'phone']
