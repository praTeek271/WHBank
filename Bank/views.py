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
    member= CustomerAccount.objects.get(id=acc)    

    if request.method=="POST":
        rname=request.POST.get("rname")
        if (rname in member.name):
            remail=request.POST.get("rEmail")
            if (remail in member.email):
                sname=request.user.username
                if (member.name ==None):
                    return(HttpResponse("<b>please Login <br>To make any Transactions...</b>"))
                else:
                    semail=request.user.username+'@gmail.com'
                    sphone=request.POST.get('sphoneno')
                    rphone=request.POST.get("rphoneno")
                    if(rphone in member.phoneno and sphone in member.phoneno):
                        sammount=request.POST.get('sammount')
                        if (member.totalbalance >sammount):
                            transfer_detail=transectiondetail(recievername=rname,recieveremail=remail,sendername=sname,senderemail=semail,deducted_amt=sammount,account_balance=(member.totalbalance-sammount))
                            transfer_detail.save()
                            member1=CustomerAccount.objects.get(name=rname) # Reciever`s id
                            print(member1)
                            member1.totalbalance=(member1.totalbalance+sammount)

                            member2=CustomerAccount.objects.get(name=sname) # Sender`s id
                            print(member2)
                            member2.totalbalance=(member1.totalbalance-sammount)
                            try:
                                member1.save() #    <----------------,
                                member2.save() #    <----------------'............(save them in the database)
                            except:
                                print("Got an Error in Saveing particular element of the database")

        else:
            return (render(request, 'Member.html', {'memberDetail':{'name':'Invalid transaction detail','email':'Please  Check your details and Try Again'}}))

    return (render(request, 'Member.html', {'memberDetail':member}))
    