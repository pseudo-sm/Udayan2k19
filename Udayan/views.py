from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import json
import pyrebase
from datetime import datetime
# Create your views here.
config = {
    'apiKey': "AIzaSyAOyWzVCElVUAqPF98altdRz5pTa-f_y9I",
    'authDomain': "udayan-7b42f.firebaseapp.com",
    'databaseURL': "https://udayan-7b42f.firebaseio.com",
    'projectId': "udayan-7b42f",
    'storageBucket': "udayan-7b42f.appspot.com",
    'messagingSenderId': "264861686730"
  };
firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()
def index(request):

    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def post_login(request):

    print(request)
    email = request.POST.get("email")
    password = request.POST.get("password")
    print(email,password)
    all = False
    return HttpResponse(json.dumps(all),content_type="application/json")
def admin(request):

    return render(request,"dashboard.html")

def photographers(request):

    return render(request,"photographers.html")

def photo_upload(request):

    return render(request,"photo.html")

def events(request):

    return render(request,"events.html")

def committee(request):

    return render(request,"committee.html")

def add_events(request):

    form = request.FILES
    name = request.POST.getlist("name[]")
    phone = request.POST.getlist("phone[]")
    email = request.POST.getlist("email[]")
    role = request.POST.getlist("role[]")
    title = request.POST.get("title")
    about = request.POST.get("about")
    branch = request.POST.get("branch")
    image = form["image"]
    prize1 = request.POST.get("prize1")
    prize2 = request.POST.get("prize2",None)
    prize3 = request.POST.get("prize3",None)
    print(name,phone,email,branch,role,title,about,image,prize1,prize2,prize3)
    for i in range(len(name)):
        db.child("events").child(branch).child(title).child("committee").child(name[i]).update({"email":email[i],"phone":phone[i],"role":role[i]})
    db.child("events").child(branch).child(title).update({"about":about,"prize1":prize1,"prize2":prize2,"prize3":prize3})
    storage.child("events").child(title).child(title).put(image)
    return HttpResponseRedirect('/events/')
def photographer_upload(request):

    auth.sign_in_with_email_and_password("photographer@gmail.com","password")
    uid = auth.current_user["localId"]
    files = request.FILES.getlist("images")
    date = str(datetime.now().date())
    i = 0
    for image in files:
        print(image)
        storage.child("photographers").child(uid).child(date).child(str(i)).put(image)
        i+=1
    return HttpResponseRedirect('/photo-upload/')