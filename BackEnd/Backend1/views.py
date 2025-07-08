from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

@login_required(login_url='')    
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
    
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1 != pass2:
            #return HttpResponse('Invalid input found.')
            messages.warning(request, "invalid input." )
            return redirect('signup')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            messages.success(request, "Congratulations !!! User registered successfully" )
        return redirect('login')
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or password incorrect")
        
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def Voting(request):
    return render(request, 'vote.html')

def contactus(request):
    return render(request, 'contact.html')

