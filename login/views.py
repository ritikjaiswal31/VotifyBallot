from django.shortcuts import render,redirect
import mysql.connector as sql
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

ad=''
pwd=''
# Create your views here.
def LogIn(request):
    global ad,pwd
    if request.method=='POST':
        mysql=sql.connect(host='localhost',user='root',password="root@1234",database='web_python_votingsystem')
        cursor=mysql.cursor()
        ad=request.POST.get('Aadhaar_no')
        pwd=request.POST.get('password')
        
        c="SELECT * FROM registration WHERE adharid='{}' AND password='{}'".format(ad,pwd)
        cursor.execute(c)
        t=cursor.fetchall()
        
        for rows in t:
            print(rows[9])
            if rows[9]==0:
                request.session['adharsession'] = ad
                return render(request,'home.html')
            else:
                messages.warning(request, "Already Voted" )
                return render(request,'login_page.html')    
        else:
            send_mail(  
                'Invalid Credentials',
                'Wrong Credentials! Please Enter Correct Credentials',
                'settings.EMAIL_HOST_USER',
                ['ritikjaiswal0256@gmail.com'],
                fail_silently = False)
            messages.warning(request, "Invalid credentials" )
            return render(request,'login_page.html')
                        
    return render(request,'login_page.html')


@login_required(login_url='login') 
def Home(request):
    return render(request,'home.html')


def Logout(request):
    logout(request)
    return redirect('login')

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')



def vote(request):
    party=request.GET.get("party")
    aid=request.session.get("adharsession")
    #print(request.GET.get("party"));
    #print(request.session.get("adharsession"))  
    mysql=sql.connect(host='database.cqtvzr6cswne.ap-south-1.rds.amazonaws.com',user='admin',password="RitikJaiswal123",database='web_python_votingsystem')
    cursor=mysql.cursor() 
    c="update registration set party='{}',status=1 where adharid='{}'".format(party,aid)
    cursor.execute(c)
    mysql.commit()
    messages.success(request, "Your vote submit successfully!!")
    return redirect('login')
    return render(request,'home,html')
def myadmin(request):
    return render(request,'admin_page.html')
def adminlogin(request):
    return render(request,'admin_page.html')    
def adminlogincheck(request):
    global ad,pwd
    if request.method=='POST':
        mysql=sql.connect(host='database.cqtvzr6cswne.ap-south-1.rds.amazonaws.com',user='admin',password="RitikJaiswal123",database='web_python_votingsystem')
        cursor=mysql.cursor()
        ad=request.POST.get('admin')
        pwd=request.POST.get('password')
        
        c="SELECT * FROM admin WHERE admin='{}' AND password='{}'".format(ad,pwd)
        cursor.execute(c)
        t=cursor.fetchall()
        
        for rows in t:
            return render(request,'adminhome.html')   
        else:
            messages.warning(request, "Invalid credentials" )
            return render(request,'admin_page.html')
                        
    return render(request,'login_page.html')        
