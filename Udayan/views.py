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

    auth.sign_in_with_email_and_password("photographer@gmail.com","password")
    return render(request,"dashboard.html")

def photographers(request):
    user = auth.current_user
    print(user)
    images = []
    dates = []
    uids = []
    photographers = []
    all_photographers = db.child("photographers").get().val()
    for photographer in all_photographers:
        for date in all_photographers[photographer]:
            no = all_photographers[photographer][date]["no"]
            for i in range(int(no)+1):
                print(storage.child("photographers").child(photographer).child(date).child(str(i)).get_url(user['idToken']))
                images.append(storage.child("photographers").child(photographer).child(date).child(str(i)).get_url(user['idToken']))
                dates.append(date)
                photographers.append(photographer)
    count = len(images)
    context = zip(photographers,dates,images,range(1,count+1))
    return render(request,"photographers.html",{"context":context})

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
    setup_cost = request.POST.get("setup_cost")
    prize2 = request.POST.get("prize2",None)
    prize3 = request.POST.get("prize3",None)
    print(name,phone,email,branch,role,title,about,image,prize1,prize2,prize3)
    for i in range(len(name)):
        db.child("events").child(branch).child(title).child("committee").child(name[i]).update({"email":email[i],"phone":phone[i],"role":role[i]})
    db.child("events").child(branch).child(title).update({"about":about,"prize1":prize1,"prize2":prize2,"prize3":prize3,"setup cost":setup_costx})
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
        db.child("photographers").child(uid).child(date).update({"no":i})
        storage.child("photographers").child(uid).child(date).child(str(i)).put(image)
        i+=1
    return HttpResponseRedirect('/photo-upload/')

def core_committee(request):


    return render(request,"core.html")
