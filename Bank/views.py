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
def Member(request,acc): #register function
    member= Account=CustomerAccount.objects.get(id=acc)  #     <----------------------    # error lies here

    if request.method=="POST":
        rname=request.POST.get("rname")
        if (member.name ==rname):
            remail=request.POST.get("rEmail")
            if (member.email==remail):
                sname=request.user.username
                if (member.name ==None):
                    return(HttpResponse("<b>please Login <br>To make any Transactions...</b>"))
                else:
                    semail=request.user.username+'@gmail.com'
                    sphone=request.POST.get('sphoneno')
                    if (member.phoneno==sphone):
                        rphone=request.POST.get("rphoneno")
                        if(member.phoneno==rphone):
                            transfer_detail=transectiondetail(recievername=rname,recieveremail=remail,sendername=sname,senderemail=semail)
                            transfer_detail.save()
        else:
            return (render(request, 'Member.html', {'memberDetail':{'name':'Invalid transaction detail','email':'Please Try Again'}}))
            
    return (render(request, 'Member.html', {'memberDetail':member}))