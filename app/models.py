from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Token(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    token=models.CharField(max_length=40)
    def __str__(self):
        return "{}_token".format(self.user)

class Expens(models.Model):
    text=models.CharField(max_length=200)
    created=models.DateTimeField(blank=True)
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
    

