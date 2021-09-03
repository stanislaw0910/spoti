from django import forms
from django.forms import TextInput, EmailInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text='Please enter your email')
    phone_number = forms.CharField(help_text='Please enter your phone number')

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2', )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
