from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=["last_name","first_name","username","email","password1"]
        