from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class FeedBack(models.Model):
    name=models.CharField(max_length=30,null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    phone=models.CharField(max_length=11,null=True, blank=True)
    desc=models.CharField(max_length=200,null=True, blank=True)
    date=models.DateField()

    def __str__(self):
        return(self.desc)

    
# class User(models.Model):
#     mame=models.CharField(max_length=30,null=True, blank=True)
#     email=models.CharField(max_length=30,null=True, blank=True)
#     Location=models.CharField(max_length=30,null=True, blank=True)


    
# class User(AbstractUser):
#     is_admin=models.BooleanField("Is admin",default=False)
#     is_employee=models.BooleanField("Is employee",default=False)
#     is_customer=models.BooleanField("Is customer",default=False)
