from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Choose a username",
        "class": "form-control",
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "Enter your email",
        "class": "form-control",
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter a strong password",
        "class": "form-control"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Repeat password",
        "class": "form-control"
    }))



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "Enter your email",
        "class": "form-control"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Enter your password",
        "class": "form-control"
    }))




