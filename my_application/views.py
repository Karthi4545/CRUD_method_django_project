from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
# Create your views here.
def home(request): # 127.0.0.1:8000
    mydata=datas.objects.all()
    if(mydata!=''):
        return render(request,'home.html',{'datas':mydata})
    else:
        return render(request,'home.html')
def addData(request):# 127.0.0.1:8000/addData
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        department=request.POST.get('department')
        email=request.POST.get('email')
        address=request.POST.get('address')

        obj=datas()
        obj.name=name
        obj.age=age
        obj.department=department
        obj.email=email
        obj.address=address
        obj.save()
        mydata=datas.objects.all()
    
        return redirect('home')
    return render(request,'home.html')
def updateData(request,id): # 127.0.0.1:8000/updateData
    mydata=datas.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        department=request.POST.get('department')
        email=request.POST.get('email')
        address=request.POST.get('address')

        mydata.name=name
        mydata.age=age
        mydata.department=department
        mydata.email=email
        mydata.address=address
        mydata.save()
        return redirect('home')  



    return render(request,'update.html',{'data':mydata})

def deleteData(request,id):   # 127.0.0.1:8000/deleteData
    mydata=datas.objects.get(id=id)
    mydata.delete()
    return redirect('home')

    