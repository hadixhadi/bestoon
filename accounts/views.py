from django.shortcuts import render ,redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            print(cd)
            User.objects.create_user(cd['username'],cd['email'],cd['password'])
            redirect('index')
    else:
        form=RegisterForm()
    return render(request,'index.html',{'form':form})   