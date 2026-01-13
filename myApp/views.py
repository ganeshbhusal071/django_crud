from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import person
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    obj=person.objects.filter(isdelete=False)
    return render(request, 'home.html',{'obj':obj, 'obj_deleted': person.objects.filter(isdelete=True)})



def form(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        city=request.POST.get('city')
        message=request.POST.get('message')
        image=request.FILES.get('image')
        p=person(name=name,email=email,age=age,city=city,message=message,image=image)
        p.save()
        send_mail(
            subject="New person added",
            message=f"{name} from {city} was created.",
            from_email=None,
            recipient_list=["zororonoa0305@gmail.com"],
            fail_silently=True,
        )
        return redirect('home')
    return render(request,'form.html')

def sendEmail(request):
    if request.method=="POST":
        subject=request.POST.get('subject')
        email=request.POST.get('email')
        message=request.POST.get('message')
        send_mail(
            subject=subject,
            message=message,
            from_email=None,
            recipient_list=[email],
            fail_silently=True,
        )
        return HttpResponse("Email sent successfully")
    return render(request,'send_email.html')

def update(request,id):
    obj=person.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        city=request.POST.get('city')
        message=request.POST.get('message')
        image=request.FILES.get('image')
        obj.name=name
        obj.email=email
        obj.age=age
        obj.city=city
        obj.message=message
        if image:
            obj.image=image
        obj.save()
        return redirect('home')
    return render(request,'update.html',{'obj':obj})

def deleteData(request,id):
    obj=person.objects.get(id=id)
    obj.isdelete=True
    obj.save()
    return redirect('home')

def hardDelete(request,id):
    obj=person.objects.get(id=id)
    obj.delete()
    return redirect('home')

def restore(request,id):
    obj=person.objects.get(id=id)
    obj.isdelete=False
    obj.save()
    return redirect('home')

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        
        if password==confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
        else:
            return HttpResponse("Password and Confirm Password do not match")
    return render(request, 'register.html')

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('home')
        return HttpResponse("Invalid username or password")
    return render(request, 'login.html')