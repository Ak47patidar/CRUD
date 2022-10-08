from rest_framework import routers
from django.urls import path, include
from ImageUpload import views
from ImageUpload.views import *


# router= routers.DefaultRouter()
# router.register(r'abc', AtulViewset)

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.home,name='image'),
    # path('api-auth/',include('rest_framework.urls')),
    # path('getdataform', views.getdataform , name='getdataform'),
    # path('postdataform', views.postdataform , name='postdataform'),
    # path('getName', views.getName , name='getName'),
    # path('postdata', views.postdata , name='postdata'),
    # path('login', views.login , name='login'),
   
]