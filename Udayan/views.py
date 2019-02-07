from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):

    return render(request,"comingsoon.html")

def admin(request):

    return render(request,"dashboard.html")
