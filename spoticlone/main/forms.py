from django import forms
from django.forms import TextInput, EmailInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Login'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            "password1": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            })

        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
