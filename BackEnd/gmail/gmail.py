def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            subject = 'Wrong Information Provided'
            message = 'Wrong Username & Password'
            email_from = 'raghavgoya059@gmail.com'
            recipient_list = ['raghavgoyal10311@gmail.com', ]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponse ("Username or password incorrect")
        
    return render(request,'login.html')
