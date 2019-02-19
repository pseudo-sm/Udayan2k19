from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import json
from django.http import JsonResponse
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

    return render(request,"index3.html")
def login(request):
    return render(request,"login.html")

def post_login(request):

    print(request)
    email = request.POST.get("email")
    password = request.POST.get("password")
    print(email,password)
    all = False
    return HttpResponse(json.dumps(all), content_type="application/json")
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

def viewevents(request):
    cse_events = dict(db.child("events").child("Computer Science & IT").get().val())
    cse_event_list = list(cse_events.keys())
    print(cse_event_list)
    return render(request,"index2.html",{"cse_event_list":cse_event_list})

def vieweventsetc(request):
    etc_events = dict(db.child("events").child("Electronics & Telecommunication").get().val())
    etc_event_list = list(etc_events.keys())
    print(etc_event_list)
    return render(request,"index2etc.html",{"etc_event_list":etc_event_list})
def vieweventseee(request):
    etc_events = dict(db.child("events").child("Electrical & Electronics").get().val())
    etc_event_list = list(etc_events.keys())
    print(etc_event_list)
    return render(request,"index2eee.html",{"etc_event_list":etc_event_list})

def vieweventsee(request):
    etc_events = dict(db.child("events").child("Electrical & Electronics").get().val())
    etc_event_list = list(etc_events.keys())
    print(etc_event_list)
    return render(request,"index2ee.html",{"etc_event_list":etc_event_list})
def vieweventsmech(request):
    etc_events = dict(db.child("events").child("Mechanical").get().val())
    etc_event_list = list(etc_events.keys())
    print(etc_event_list)
    return render(request,"index2mech.html",{"etc_event_list":etc_event_list})
def vieweventscivil(request):
    etc_events = dict(db.child("events").child("Civil").get().val())
    etc_event_list = list(etc_events.keys())
    print(etc_event_list)
    return render(request,"index2civil.html",{"etc_event_list":etc_event_list})
def cse(request,event_name):


    faculty = []
    students = []
    cse_events = dict(db.child("events").child("Computer Science & IT").get().val())
    about = (cse_events[event_name]["about"])
    prize1 = (cse_events[event_name]["prize1"])
    prize2 = (cse_events[event_name]["prize2"])
    committee_members = dict(cse_events[event_name]["committee"])

    for name in committee_members:
        if committee_members[name]["role"] == "Faculty":
            faculty.append({"email":committee_members[name]["email"],"phone":committee_members[name]["phone"],"name":name})
        else:
            students.append({"email":committee_members[name]["email"],"phone":committee_members[name]["phone"],"name":name})
    print(faculty)
    print(students)
    cse_event_list = list(cse_events.keys())
    print(cse_event_list)
    return render(request,"cse.html",{"about":about,"prize1":prize1,"prize2":prize2,"faculty":faculty,"students":students,"event_name":event_name})

def etc(request,event_name):


    faculty = []
    students = []
    cse_events = dict(db.child("events").child("Electronics & Telecommunication").get().val())
    about = (cse_events[event_name]["about"])
    prize1 = (cse_events[event_name]["prize1"])
    prize2 = (cse_events[event_name]["prize2"])
    committee_members = dict(cse_events[event_name]["committee"])

    for name in committee_members:
        if committee_members[name]["role"] == "Faculty":
            faculty.append({"email":committee_members[name]["email"],"phone":committee_members[name]["phone"],"name":name})
        else:
            students.append({"email":committee_members[name]["email"],"phone":committee_members[name]["phone"],"name":name})
    print(faculty)
    print(students)
    cse_event_list = list(cse_events.keys())
    print(cse_event_list)
    return render(request,"cse.html",{"about":about,"prize1":prize1,"prize2":prize2,"faculty":faculty,"students":students,"event_name":event_name})

def eee(request,event_name):


    faculty = []
    students = []
    cse_events = dict(db.child("events").child("Electrical & Electronics").get().val())
    about = (cse_events[event_name]["about"])
    prize1 = (cse_events[event_name]["prize1"])
    prize2 = (cse_events[event_name]["prize2"])
    committee_members = dict(cse_events[event_name]["committee"])

    for name in committee_members:
        if committee_members[name]["role"] == "Faculty":
            faculty.append({"email":committee_members[name]["email"],"phone":committee_members[name]["phone"],"name":name})
        else:
            students.append({"email":committee_members[name]["email"],"phone":committee_members[name]["phone"],"name":name})
    print(faculty)
    print(students)
    cse_event_list = list(cse_events.keys())
    print(cse_event_list)
    return render(request,"cse.html",{"about":about,"prize1":prize1,"prize2":prize2,"faculty":faculty,"students":students,"event_name":event_name})

def ee(request,event_name):


    faculty = []
    students = []
    cse_events = dict(db.child("events").child("Electrical & Electronics").get().val())
    about = (cse_events[event_name]["about"])
    prize1 = (cse_events[event_name]["prize1"])
    prize2 = (cse_events[event_name]["prize2"])
    committee_members = dict(cse_events[event_name]["committee"])

    for name in committee_members:
        if committee_members[name]["role"] == "Faculty":
            faculty.append({"email":committee_members[name]["email"],"phone":committee_members[name]["phone"],"name":name})
        else:
            students.append({"email":committee_members[name]["email"],"phone":committee_members[name]["phone"],"name":name})
    print(faculty)
    print(students)
    cse_event_list = list(cse_events.keys())
    print(cse_event_list)
    return render(request,"cse.html",{"about":about,"prize1":prize1,"prize2":prize2,"faculty":faculty,"students":students,"event_name":event_name})

def mech(request,event_name):


    faculty = []
    students = []
    cse_events = dict(db.child("events").child("Mechanical").get().val())
    about = (cse_events[event_name]["about"])
    prize1 = (cse_events[event_name]["prize1"])
    prize2 = (cse_events[event_name]["prize2"])
    committee_members = dict(cse_events[event_name]["committee"])

    for name in committee_members:
        if committee_members[name]["role"] == "Faculty":
            faculty.append({"email":committee_members[name]["email"],"phone":committee_members[name]["phone"],"name":name})
        else:
            students.append({"email":committee_members[name]["email"],"phone":committee_members[name]["phone"],"name":name})
    print(faculty)
    print(students)
    cse_event_list = list(cse_events.keys())
    print(cse_event_list)
    return render(request,"cse.html",{"about":about,"prize1":prize1,"prize2":prize2,"faculty":faculty,"students":students,"event_name":event_name})

def civil(request,event_name):


    faculty = []
    students = []
    cse_events = dict(db.child("events").child("Civil").get().val())
    about = (cse_events[event_name]["about"])
    prize1 = (cse_events[event_name]["prize1"])
    prize2 = (cse_events[event_name]["prize2"])
    committee_members = dict(cse_events[event_name]["committee"])

    for name in committee_members:
        if committee_members[name]["role"] == "Faculty":
            faculty.append({"email":committee_members[name]["email"],"phone":committee_members[name]["phone"],"name":name})
        else:
            students.append({"email":committee_members[name]["email"],"phone":committee_members[name]["phone"],"name":name})
    print(faculty)
    print(students)
    cse_event_list = list(cse_events.keys())
    print(cse_event_list)
    return render(request,"cse.html",{"about":about,"prize1":prize1,"prize2":prize2,"faculty":faculty,"students":students,"event_name":event_name})


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
    db.child("events").child(branch).child(title).update({"about":about,"prize1":prize1,"prize2":prize2,"prize3":prize3,"setup cost":setup_cost})
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

def demo(request):

    return render(request,"demo/demo.html")

def feed(request):

    return render(request,"feed.html")
def sponsorship(request):

    return render(request,"sponsorship.html")


def technical(request):

    regno = ['1501289324','1501289391','1501289419','1501289048','1501289094','1501289125','1501289111','1501289197','1501289278','1501289323']
    name = ['ABHISHEK BHOLA','SWADHIN KUMAR SENAPATI','ARPAN KUMAR SAMANTARAY','PRATIK DASMAHAPATRA','SUVANKAR SAHU','ASHISH KAMANI','AISHWARYA NAYAK','RISHAV KUMAR','SAROJ KUMAR SAHOO','SRIPATI SAGAR PATTNAYAK']
    branch = ['ETC','ETC','MECH-A','MECH-B','CIVIL','CSE','CSE','CSE','EEE','EE']
    phone = ['7008068053','8908408558','7008352085','7008716401','7381180506','9776448769','8018531094','7008607895','7873900425','9040890544']
    email = ['abhishekbholatat@gmail.com','kumar.swadhin9777@gmail.com','arpankumarsamantaray7@gmail.com','pratikdasmahapatra71@gmail.com','araj90755@gmail.com','kamaniashis17@gmail.com','aishatat991@gmail.com','rishav74492644@gmail.com','belongstosaroj98@gmail.com','sagarpattnayak10@gmail.com']
    images = ['../static/Assets/Images/Committee/bhola.png','../static/Assets/Images/Committee/aaa.png','../static/Assets/Images/Committee/Arpan Kumar Samantaray.jpg','../static/Assets/Images/Committee/Pratik Dasmahapatra.jpg','../static/Assets/Images/Committee/SUBHANKAR 4-3.jpg','../static/Assets/Images/Committee/as.jpg','https://s3.amazonaws.com/uifaces/faces/twitter/adhamdannaway/128.jpg','../static/Assets/Images/Committee/IMG_20190108_123234.jpg','https://s3.amazonaws.com/uifaces/faces/twitter/adhamdannaway/128.jpg','https://s3.amazonaws.com/uifaces/faces/twitter/adhamdannaway/128.jpg']
    print(len(images),len(name))
    context = zip(regno,name,branch,phone,email,images)
    return render(request,"technical.html",{"context":context})

def sponsors(request):

    names = ['Abhinash Dhal','Bidhu Bhusan Dash','Biswajeet Mangaraj','Adarsh Mohanty','Chinmayee Mekup','Sailesh Mahapatra','Bibhuti Swain','Abhinash Dash','Sk. Fukkaran Ali','Shaswat Sucharit Patnaik']
    branch = ['ETC','ETC','CSE','CSE','CSE & IT','MECH','MECH','CIVIL','EEE','EE']
    phone = ['7609937976','7008412591','9348910702','9090154358','8280474863','7008111430','7978619955','9124457352','8984873440','8658138404']
    images = []
    for i in range(len(names)):
        images.append('https://s3.amazonaws.com/uifaces/faces/twitter/adhamdannaway/128.jpg')
    context = zip(names,branch,phone,images)
    return render(request,"sponsors.html",{"context":context})
def publicity(request):

    names = ['Shahnawaz','Prasanjeet Behera','Kishan Kumar Sahoo','Satyajit Samal','Suraj Kumar Behera','Sandeep Rana']
    branch  =['CSE','ETC','CIVIL','MECH','EE','CSE']
    phone = ['7091500323','750438327','8457043036','8093522413','8917439355','9853437782']
    images = []
    for i in range(len(names)):
        images.append('https://s3.amazonaws.com/uifaces/faces/twitter/adhamdannaway/128.jpg')
    context = zip(names,branch,phone,images)
    return render(request,"publicity.html",{"context":context})

def sponsorsship(request):


    return render(request,"sponsors.html")



def events_api(request):

    take = request.GET.get("branch")
    response = {'success':'y'}
    tempresp = []
    if take == '0':
        branch = "Computer Science & IT"
    elif take == '1':
        branch = 'Civil'
    elif take == '3':
        branch = 'Electrical & Electronics'
    elif take == '2':
        branch = 'Mechanical'
    elif take == '4':
        branch = 'Electronics & Telecommunication'
    events = dict(db.child("events").child(branch).get().val())
    ind_event = []
    studentname=[]
    studentemail=[]
    studentphone=[]
    facultyname=[]
    facultyemail=[]
    facultyphone=[]
    for event in events:
        events[event].update({"eventname":event})
        for member in events[event]["committee"]:
            if events[event]["committee"][member]["role"] == "Student":
                studentemail.append(events[event]["committee"][member]["email"])
                studentphone.append(events[event]["committee"][member]["phone"])
                studentname.append(member)
            else:
                facultyemail.append(events[event]["committee"][member]["email"])
                facultyphone.append(events[event]["committee"][member]["phone"])
                facultyname.append(member)
        tempresp.append({"eventname":event,"about":events[event]["about"],"prize1":events[event]["prize1"],"prize2":events[event]["prize2"],"faculty_coordinator":facultyname,"faculty_contact":facultyphone,"faculty_email":facultyemail,"student_coordinator":studentname,"student_contact":studentphone,"student_email":studentemail})

    response.update({branch:tempresp})
    return JsonResponse(response,safe=False)
