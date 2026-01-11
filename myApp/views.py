from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import person

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
        return redirect('home')
    return render(request,'form.html')

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