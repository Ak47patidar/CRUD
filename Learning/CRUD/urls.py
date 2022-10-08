import imp
from rest_framework import routers
from django.urls import path, include
from CRUD import views
from CRUD.views import AtulViewset


router= routers.DefaultRouter()
router.register(r'abc', AtulViewset)

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.home,name='home'),
    path('api-auth/',include('rest_framework.urls')),
    path('getdataform', views.getdataform , name='getdataform'),
    path('postdataform', views.postdataform , name='postdataform'),
    path('getName', views.getName , name='getName'),
    path('postdata', views.postdata , name='postdata'),
    path('login', views.login , name='login'),
   
]
