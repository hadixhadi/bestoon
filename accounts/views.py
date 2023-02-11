from django.shortcuts import render ,redirect
from .forms import RegisterForm ,LoginForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate ,login
from app import urls
from django.contrib import messages
# Create your views here.
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            print(cd)
            User.objects.create_user(cd['username'],cd['email'],cd['password'])
            messages.success(request,"user created")
            return redirect('login')
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
                messages.success(request , "loged in")
                return redirect('index')
            else:
                print("erore")
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

