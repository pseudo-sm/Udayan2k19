from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):

    return render(request,"comingsoon.html")

def admin(request):

    return render(request,"dashboard.html")

def photographers(request):

    return render(request,"photographers.html")

def photo_upload(request):

    return render(request,"photo.html")

def events(request):

    return render(request,"events.html")
