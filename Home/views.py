from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from product.models import CakePr
# Create your views here.
def ind(request):
    return render(request,'test.html')
def index(request):
    #data=CakePr.objects.get(id=2)  #o-r-m for database(select * from table where id=2);  get is used to call a specific product
    data=CakePr.objects.all()          #all is used to select all the product.
    return render(request,'index.html',{'data':data})

def log(request):
    if request.method=="POST":
        uname=request.POST['uname']
        pname=request.POST['password']
        user=auth.authenticate(username=uname,password=pname) #username password in the table 
        if user is not None:
            auth.login(request,user)        #permission giving process
       
            return redirect("/")
        else:
            message="*invalid username and password"

        return render(request,"login.html",{'msg':message})        #here request has url    
    else:
        return render(request,'login.html')


def reg(request):
    if request.method=="POST":
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        Email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['repassword']
        if password==repassword:
            if User.objects.filter(username=uname).exists():
                msg="the user name is already taken"
            elif User.objects.filter(email=Email).exists(): 
                msg="the email already exsist"
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=Email,password=repassword)
                user.save()
                auth.login(request,user)  #automatically login after the registration.
                msg="Registration successfull"
                return redirect("/")
        else:
            msg="*password not same"
        return render(request,"register.html",{"msge":msg})
    else:
        return render(request,'register.html')
    

def logt(request):
        auth.logout(request)
        return redirect('/')
        #return render(request,'test.html')






































"""def logsub(request):
    uname=request.POST['uname']
    pname=request.POST['password']
    user=auth.authenticate(username=uname,password=pname) #username password in the table 
    if user is not None:
        auth.login(request,user)        #permission giving process
       
        return redirect("/")
    else:
        message="*invalid username and password"

        return render(request,"login.html",{'msg':message})        #here request has url    

#def regsub(request):
    uname=request.POST['uname']
    fname=request.POST['fname']
    lname=request.POST['lname']
    Email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']
    if password==repassword:
        if User.objects.filter(username=uname).exists():
            msg="the user name is already taken"
        elif User.objects.filter(email=Email).exists(): 
            msg="the email already exsist"
        else:
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=Email,password=repassword)
            user.save()
            auth.login(request,user)  #automatically login after the registration.
            msg="Registration successfull"
            return redirect("/")
    else:
        msg="*password not same"

    return render(request,"register.html",{"msge":msg})"""
