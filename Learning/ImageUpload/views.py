from django.http import HttpResponse
from django.shortcuts import render
from ImageUpload.models import ImageModel
from rest_framework import viewsets
from ImageUpload.serializer import ImageSerializer

class ImageViewset(viewsets.ModelViewSet):
    queryset= ImageModel.objects.all()
    serializer_class= ImageSerializer 

def home(request):
     return render(request, 'home.html')

def Imageview(request):
    if request.method=='post':
        obj=ImageModel()
        obj.id = request.POST['name']
        obj.Profile_pic = request.POST['image']
        obj.save()
    return HttpResponse("Data saved successfully")