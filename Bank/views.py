from django.http import HttpResponse
from django.shortcuts import render,redirect
from Bank.models import FeedBack as feed
from datetime import datetime
from .models import CustomerAccount,transectiondetail

def homepage(request):
    
    return (render(request,'Homepage.html'))


def viewMember(request):

    Account=CustomerAccount.objects.all()
    if Account is None:
        parmas={'acc':"No dataset created yet"}
    else:
        params={'acc':Account}
    return (render(request,'MemberView.html',params))

    # def customers(request):
    #     customers = customerdetail.objects.all()
    #     if request.method == "POST":
    #         email = request.POST.get('email')
    #         semail = request.POST.get('semail')
    #         amt = request.POST.get('amt')
    #         try:
    #             amt = int(amt)
    #         except:
    #             print("enter amount")
    #         for i in customers:
    #             print(email)
    #             if i.email == email:
    #                 j = i
    #                 id = i.id
    #                 break
    #         for i in customers:
    #             print(i.email,i.avail_bal,semail)
    #             if i.email==semail and amt< i.avail_bal and amt>0 :
    #                 avail_bal = i.avail_bal - amt
    #                 avail_bal2 = j.avail_bal + amt
    #                 try:
    #                     query1 = transectiondetail(name=i.name, email=i.email,
    #                                                 deb_amt=amt ,cr_amt=0 , ac_bal=avail_bal)

    #                     query2 = customerdetail(id=i.id, avail_bal=avail_bal, email=i.email
    #                                                     , name=i.name)
    #                     query3 = transectiondetail(name=j.name, email=j.email,
    #                                                 deb_amt=0 ,cr_amt=amt , ac_bal=avail_bal2)
    #                     query4 = customerdetail(id=id, avail_bal=avail_bal2, email=j.email
    #                                                     , name=j.name)
    #                     query2.save()
    #                     query1.save()
    #                     query4.save()
    #                     query3.save()
                        
    #                     return redirect('/customers')


    #                     break
    #                 except:
    #                     print("transection failed")
    #                     break
    #         else:
    #             print("invalid data")

def FeedBackUs(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("Email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        feedback=feed(name=name,email=email,phone=phone,desc=desc,date=datetime.now())
        feedback.save()

    parms={'namert':"hello from views  .py file"}
    return (render(request,'feedback.html',parms))

# --------------------------------------------------------------------------
def signup(request): #register function
    msg=None
    # if request.method=='POST':
    #     form=SignUpForm(request.POST)
    #     if (form.is_valid()):
    #         user=   form.save()
    #         msg='New User Account Created'
    #         return(redirect(loginFEAT))
    #     else:
    #         msg='Login Form Not Valid Error'

    # else:
    #     form=SignUpForm()
    form="hello from form"
    return (render(request,'register.html',{'form':form,'msg':msg}))
   
    
def loginFEAT(request):
    # form=LoginForm(request.POST or None)
    msg=None
    # if (request.method=='POST'):
    #     if form.is_valid():
    #         username=form.cleaned_data.get('username')
    #         password=form.cleaned_data.get('password')
    #         user=authenticate(username=username,password=password)
    #         if user is not None:
    #             login(request, user)
    #             return(redirect('homepage',{'userName':'Admin'}))
    #         elif user is not None and user.is_customer:
    #             login(request, user)
    #             return(redirect('homepage',{'userName':'Customer'}))
    #         elif user is not None and user.is_employee:
    #             login(request, user)
    #             return(redirect('homepage',{'userName':'Employee'}))
    #         else:
    #             msg='Invalid UserName and Password'
            
    #     else:
    #         msg='Error in Account Verification  !'
    form="hello from form"
    return (render(request,'login.html',{'forms':form,'msg':msg})) 

def logoutFEAT(request):
    
    return (render(request,'Homepage.html'))

# -------------------------------------------------------------------------------

