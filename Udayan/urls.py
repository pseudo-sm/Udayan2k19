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
    url(r'feed/',views.feed,name="feed"),
    url(r'demo/',views.demo,name="demo"),
    url(r'login/',views.login,name="login"),
    url(r'post-login/',views.post_login,name="post_login"),
    url(r'photo-upload/',views.photo_upload,name="photo_upload"),
    url(r'photographers/',views.photographers,name="photographers"),
    url(r'upload/',views.photographer_upload,name="photographer_upload"),
    url(r'events/',views.events,name="events"),
    url(r'^cse/(?P<event_name>\w.*)/', views.cse, name="cse"),
    url(r'^etc/(?P<event_name>\w.*)/', views.etc, name="etc"),
    url(r'^ee/(?P<event_name>\w.*)/', views.eee, name="ee"),
    url(r'^eee/(?P<event_name>\w.*)/', views.ee, name="eee"),
    url(r'^mech/(?P<event_name>\w.*)/', views.mech, name="mech"),
    url(r'^civil/(?P<event_name>\w.*)/', views.civil, name="civil"),
    url(r'photographer-upload/',views.photographer_upload,name="photographer_upload"),
     url(r'feed/',views.feed,name="feed"),
    url(r'viewevent/',views.viewevents,name="viewevents"),
    url(r'vieweventetc/',views.vieweventsetc,name="vieweventsetc"),
    url(r'vieweventeee/',views.vieweventseee,name="vieweventseee"),
    url(r'vieweventee/',views.vieweventsee,name="vieweventsee"),
    url(r'vieweventmech/',views.vieweventsmech,name="vieweventsmech"),
    url(r'vieweventcivil/',views.vieweventscivil,name="vieweventscivil"),
    url(r'^add-event/',views.add_events,name="addevent"),
    url(r'^committee/',views.committee,name="committee"),
    url(r'^core-committee/',views.core_committee,name="core_committee"),
    url(r'',views.index,name="index"),


]
