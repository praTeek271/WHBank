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
  
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30,null=True, blank=True)
    account_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to='media/', default="Image003.png")
    totalbalance=models.IntegerField(default=1000)
    phoneno=models.CharField(max_length=11,blank=True)
    
    def __str__(self):
        return(f"{self.id}--{self.name} ------------> Status :{self.account_active}".format(self.id,self.name,self.account_active))


class transectiondetail(models.Model):
    sendername = models.CharField(max_length=30,default="anonymous")
    senderemail = models.EmailField(max_length=30,blank=False,default="anonymous@anonymous.com")
    recievername = models.CharField(max_length=30,default="anonymous")
    recieveremail = models.EmailField(max_length=30,blank=False,default="anonymous@anonymous.com")
    deducted_amt = models.IntegerField(default=0)
    credited_amt = models.IntegerField(default=0)
    account_balance = models.IntegerField(default=1000)

    def __str__(self):
        return(f"{self.sendername}  -- to -->    {self.recievername}".format(self.sendername,self.recievername))

#---------------------------------------------------------------------------------------------------------------
