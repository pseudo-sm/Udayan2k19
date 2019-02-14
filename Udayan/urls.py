"""pdoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'admin/',views.admin,name="admin"),
    url(r'login/',views.login,name="login"),
    url(r'post-login/',views.post_login,name="post_login"),
    url(r'photo-upload/',views.photo_upload,name="photo_upload"),
    url(r'photographers/',views.photographers,name="photographers"),
    url(r'upload/',views.photographer_upload,name="photographer_upload"),
    url(r'events/',views.events,name="events"),
    url(r'^cse/', views.cse, name="cse"),
    url(r'photographer-upload/',views.photographer_upload,name="photographer_upload"),
    url(r'viewevent/',views.viewevents,name="viewevents"),
    url(r'^add-event/',views.add_events,name="addevent"),
    url(r'^committee/',views.committee,name="committee"),
    url(r'^core-committee/',views.core_committee,name="core_committee"),
    url(r'',views.index,name="index"),


]
