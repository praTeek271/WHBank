from django.http import HttpResponse
from django.shortcuts import render,redirect
from Bank.models import FeedBack as feed
from datetime import datetime
# from .forms import SignUpForm,LoginForm

from django.contrib.auth import authenticate,login,logout


def homepage(request):
    
    return (render(request,'Homepage.html'))


def viewMember(request):
    # params={'accid':'accid Input  '}
    return (render(request,'MemberView.html'))


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

