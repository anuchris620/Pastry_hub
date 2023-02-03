from django.shortcuts import render,redirect
from django.contrib.auth.models import auth

# Create your views here.
def ind(request):
    return render(request,'test.html')
def index(request):
    return render(request,'index.html')
def log(request):
    return render(request,'login.html')

def reg(request):
    return render(request,'register.html')

def logsub(request):
    uname=request.GET['uname']
    pname=request.GET['password']
    user=auth.authenticate(username=uname,password=pname) #username password in the table 
    if user is not None:
        auth.login(request,user)        #permission giving process
        msg="login successfully"
        return redirect("/")
    else:
        msg="invalid username and password"
    
        return render(request,'test.html',{'s':msg})         #here request has url    