from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class RegisterForm(UserCreationForm):
#     email=forms.EmailField(required=True)
#     class Meta:
#         model=User
#         fields=['username','email','password1','password2']



class RegisterForm(forms.Form):
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    password=forms.CharField(max_length=50)

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    