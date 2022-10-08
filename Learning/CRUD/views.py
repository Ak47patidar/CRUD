from django.shortcuts import render, HttpResponse,redirect
from rest_framework import viewsets
from .CRUD_Serializer import AtulSerializer
from .models import AtulModel
from Learning.middlewares.auth import auth_Middleware
import Learning

class AtulViewset(viewsets.ModelViewSet):
    queryset= AtulModel.objects.all()
    serializer_class= AtulSerializer   


def home(request):
    return render(request, 'login.html')

@auth_Middleware
def login(request):    
    id = request.POST['id']
    name = request.POST['name']

    obj= AtulModel.objects.get(id=id)
    if obj.name==name:
        request.session['user_id']=obj.id
        request.session['user_name']=obj.name
        print("Your name stored in cache is-", request.session.get('user_name'))
        return render(request,'base.html',{'name':name})
    else:
        return HttpResponse("Invalid Username or password")
    


def getdataform(request):
    return render(request, 'getdata.html')

def postdataform(request):
    return render(request, 'postdata.html')

def getName(request):   
    id= request.POST['id']
    res1= AtulModel.objects.get(id=id)
    res=res1.name
    return render (request, 'name.html',{'name':res})

def postdata(request):
    id=request.POST['id']
    name=request.POST['name']
    data=AtulModel(id=id, name=name)
    data.save()
    return HttpResponse("Data successfully uploaded")