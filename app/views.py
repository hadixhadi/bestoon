from django.shortcuts import render
from .models import Expens,Income,Token
import json
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Expens , Token , Income ,User
from datetime import datetime
@csrf_exempt
def submit_expense(request):
    this_token=request.POST['token']
    this_user=User.objects.filter(token__token= this_token).get()
    now=datetime.now()
    Expens.objects.create(text=request.POST['text'],created=now,
                          amount=request.POST['amount'], user=this_user)
    print(request.POST)
    return JsonResponse({
        'status':'ok'
    },encoder=JSONEncoder)
   

@csrf_exempt
def submit_income(request):
    this_token=request.POST['token']
    this_user=User.objects.filter(token__token= this_token).get()
    now=datetime.now()
    Income.objects.create(text=request.POST['text'],created=now,
                          amount=request.POST['amount'], user=this_user)
    print(request.POST)
    return JsonResponse({
        'status':'ok'
    },encoder=JSONEncoder)