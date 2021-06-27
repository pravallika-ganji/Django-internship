"""FirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FirstApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('he/',htmltag),
    path('usr/<str:uname>/',usernameprint),
    path('usag/<str:un>/<int:ag>/',usernameage),
    path('emp/<str:eid>/<int:eage>/<str:ename>/',empdetails),
    path('ht/',htm),
    path('yt/<str:name>/',ytname),
    path('pt/<int:id>/<str:ename>/',empname),
    path('stud/',studentdetails),
    path('internalJS/',internalJS),
    path('myform/',myform,name='myform'),
    path('signup/',signup, name='signup'),
    path('boot/',bootstrapfun),
    path('btrg/',btregi,name='btr'),
    path('register1/',register1),
    path('register2/',register2,name= "register2"),
    path('display/',display,name="dt"),
     path('display/',views.display,name="dt"),
    path('viw/<int:y>/',views.sview,name="sv"),
    path('upu/<int:q>/',views.supt,name="sup"),
    path('dl/<int:p>/',views.sudl,name="sd"),
]
