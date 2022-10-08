from atexit import register
from django.contrib import admin
from .models import AtulModel

admin.site.register(AtulModel)

# Username=admin Password=admin
