from asyncio import QueueEmpty
from dataclasses import field
import imp
from msilib.schema import Class
from pyexpat import model
from rest_framework import serializers
from .models import AtulModel

class AtulSerializer(serializers.ModelSerializer):
    class Meta:
        model=AtulModel
        fields=('id','name')

