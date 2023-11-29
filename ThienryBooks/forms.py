from django.forms import ModelForm
from ThienryBooks.models import Hiring, Exchange
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ParentForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class HiringForm(ModelForm):
    class Meta:
        model = Hiring
        fields = '__all__'
        widgets = {
            'official_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Official Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Location'}),
            'price': forms.TextInput(attrs={' class ': 'form-control', 'placeholder': 'Price To Hire'}),
            'description': forms.TextInput(attrs={'class ': 'form-control', 'placeholder': 'Descriptions'}),

        }


class ExchangeForm(ModelForm):
    class Meta:
        model = Exchange
        fields = '__all__'
        widgets = {
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Official Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'book_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Title'}),
            'book_author': forms.TextInput(attrs={' class ': 'form-control', 'placeholder': 'Book Author'}),
            'book_needed': forms.TextInput(attrs={'class ': 'form-control', 'placeholder': 'Book Needed'}),

        }


