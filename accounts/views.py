from django.shortcuts import render ,redirect
from .forms import RegisterForm , LoginForm 
from app.models import Token
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate ,login
from app import urls
from django.contrib import messages
from django.utils.crypto import get_random_string
# Create your views here.
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            newuser=User.objects.create_user(cd['username'],cd['email'],cd['password'])
            this_token=get_random_string(length=40)
            Token.objects.create(user=newuser,token=this_token)
            contex={
                'message':'this is your Token {}'.format(this_token)
            }
            return render(request,'home.html',contex)
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})  

@csrf_exempt
def loginPage(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                print("erore")
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

