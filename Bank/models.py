from django.db import models

# Create your models here.
class FeedBack(models.Model):
    name=models.CharField(max_length=30,null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    phone=models.CharField(max_length=11,null=True, blank=True)
    desc=models.CharField(max_length=200,null=True, blank=True)
    date=models.DateField()

    def __str__(self):
        return(self.desc)

    
class CustomerAccount(models.Model):
    # CR_ID=models.IntegerField()
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30,null=True, blank=True)
    account_active=models.BooleanField(default=True)
#     customer_image=models.ImageField(upload_to='customer_img', default="")
# class CoustomerFeedBack(models.Model):
#     CUname=models.CharField(max_length=30,null=True, blank=True)
#     CUemail=models.EmailField(null=True, blank=True)
#     CUphone=models.CharField(max_length=11,null=True, blank=True)
#     CUdesc=models.CharField(max_length=200,null=True, blank=True)
#     CUdate=models.DateField()


class transectiondetail(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    deducted_amt = models.IntegerField()
    credited_amt = models.IntegerField()
    account_balance = models.IntegerField()

#---------------------------------------------------------------------------------------------------------------
