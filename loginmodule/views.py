from django.shortcuts import render,redirect
from .models import studentdetails,maintooltable,requestt
from django.contrib.auth.models import User,auth
import array as arr

# Create your views here.
def home(request):
    return render(request,'studentlogin.html')


def studentlogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if user.username.startswith('kct'):
                return render(request,'staff.html')
            else:

                name=user.first_name
                return render(request,'studenthomepage.html',{'name':name})
        else:
            mess="credentials does not match"
            return render(request,'studentlogin.html',{'mess':mess})
    else:
        return render(request,'studentlogin.html')

def logout(request):
    auth.logout(request)
    return redirect('studentlogin')
def staff(request):
    return render(request,'staff.html')

def studentregister(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        rollno=request.POST['rollno']
        department=request.POST['department']
        year=request.POST['year']
        phone=request.POST['phone']
        hs=request.POST['hs']
        city=request.POST['city']
        pphone=request.POST['pphone']
        username=request.POST['rollno']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            user=User.objects.create_user(first_name=firstname,last_name=lastname,username=rollno,password=password1)
            user.save()
            det=studentdetails(firstname=firstname,lastname=lastname,rollno=rollno,department=department,year=year,phoneno=phone,
                                           hs=hs,city=city,parent_phoneno=pphone,username=username,password=password1)
            det.save()
            return redirect('studentlogin')
        else:
            mess="password does not match"
            return render(request,'studentregistration.html',{'mess':mess})
    else:
        return render(request,'studentregistration.html')

def staffphysics(request):
    
    return render(request,'physicspage.html')
def components(request):
    return render(request,'component.html')

def add(request):
    toolname=request.POST['toolname']
    subject=request.POST['subject']
    totalquantity=request.POST['totalquantity']
    a=maintooltable(name=toolname,subject=subject,total_quantity=totalquantity,available_now=totalquantity)
    a.save()
    return redirect('components')

def staffchemistry(request):
    return render(request,'chemistrypage.html')
def studentphysics(request):
    tools=maintooltable.objects.filter(subject="physics")
    return render(request,'studentphysics.html',{'tool':tools})
def req(request):
    return render(request,'requestingpage.html')
def requesting(request):
    
    
    quantity=request.POST['amt']
    t=request.POST['tool']
    o=maintooltable.objects.get(name=t)
    sub=o.subject
    g=maintooltable.objects.get(name=t)
    name=request.user.username
    s=studentdetails.objects.get(username=name)
    
    status="requested"
    send=requestt(subject=o.subject,tool=t,toolname=g,quantity_req=quantity,status=status,name=s)
    send.save()

    return redirect('studentphysics')
def requestdetails(request):
    g=requestt.objects.filter(name=request.user.username)
    return render(request,'requestdetails.html',{'g':g})
def studenthomepage(request):
    name=request.user.first_name
    return render(request,'studenthomepage.html',{'name': name})

def studentchemistry(request):
    tools=maintooltable.objects.filter(subject="chemistry")
    return render(request,'studentphysics.html',{'tool':tools})
def staffp(request):
    m=requestt.objects.filter(subject="physics")
    for a in m: 
       a.status="requested"
       a.save()
    return render(request,'staffrequest.html',{'m':m})

    