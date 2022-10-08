from asyncio import QueueEmpty
from dataclasses import field
import imp
from msilib.schema import Class
from pyexpat import model
from rest_framework import serializers
from ImageUpload.models import ImageModel

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImageModel
        fields= '__all__'  