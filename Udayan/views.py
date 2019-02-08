from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import json
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

def add_events(request):

    form = request.FILES
    name = request.POST.getlist("name[]")
    phone = request.POST.getlist("phone[]")
    event = request.POST.getlist("event[]")
    email = request.POST.getlist("email[]")
    department = request.POST.getlist("department[]")
    title = request.POST.get("title")
    about = request.POST.get("about")
    image = form["image"]
    print(name,phone,event,email,department,about,image,title)
    return HttpResponseRedirect('/events/')
