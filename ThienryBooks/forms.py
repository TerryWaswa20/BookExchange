from django.forms import ModelForm
from ThienryBooks.models import Parent, Hiring, Purchase
from django import forms


class ParentForm(ModelForm):

    class Meta:
        model = Parent
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'confirm_password')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Create Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Set Password'}),
            'confirm_password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),

        }


class HiringForm(ModelForm):
    class Meta:
        model = Hiring
        fields = '__all__'
        widgets = {
            'official_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Official Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Location'}),

        }


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'


