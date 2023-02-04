from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expens(models.Model):
    text=models.CharField(max_length=200)
    created=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return "{} : {} - {} -{}".format(self.user,self.text,self.amount,self.created)
    

class Income(models.Model):
    text=models.CharField(max_length=200)
    created=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return "{} : {} - {} -{}".format(self.user,self.text,self.amount,self.created)    
    

