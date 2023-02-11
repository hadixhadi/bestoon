from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# class RegisterForm(UserCreationForm):
#     firstName=forms.CharField(max_length=50)
#     LastName=forms.CharField(max_length=50)
#     email=forms.EmailField()
#     class Meta:
#         model=User
#         fields=['username','firstName','LastName','email','password1','password2']



class RegisterForm(forms.Form):
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    password=forms.CharField(max_length=50)

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    