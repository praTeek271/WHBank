from django.http import HttpResponse
from django.shortcuts import render,redirect
from Bank.models import FeedBack as feed
from datetime import datetime
from .models import CustomerAccount,transectiondetail

def homepage(request):
    Accname=request.user.username
    return (render(request,'Homepage.html',{'username':Accname}))


def viewMember(request):
    Accname=request.user.username
    Account=CustomerAccount.objects.all()
    if Account is None:
        parmas={'acc':"No dataset created yet",'username':Accname}
    else:
        params={'acc':Account,'username':Accname}
    return (render(request,'MemberView.html',params))

def FeedBackUs(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("Email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        feedback=feed(name=name,email=email,phone=phone,desc=desc,date=datetime.now())
        feedback.save()
    Accname=request.user.username
    
    parms={'username':Accname}
    return (render(request,'feedback.html',parms))

# --------------------------------------------------------------------------
def signup(request): #register function
    msg=None
    form="hello from form"
    return (render(request,'register.html',{'form':form,'msg':msg}))
   
    
def loginFEAT(request):

    msg=None
    form="hello from form"
    return (render(request,'login.html',{'forms':form,'msg':msg})) 

def logoutFEAT(request):
    
    return (render(request,'Homepage.html'))

# -------------------------------------------------------------------------------

