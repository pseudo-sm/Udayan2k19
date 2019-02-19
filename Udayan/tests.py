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


def events_api(request):

    response = {'success':'y'}
    events = dict(db.child("events").get().val())
    for branch in events:
        ind_event = []
        studentname=[]
        studentemail=[]
        studentphone=[]
        facultyname=[]
        facultyemail=[]
        facultyphone=[]
        for event in events[branch]:
            events[branch][event].update({"eventname":event})
            ind_event.append(events[branch][event])
        response.update({branch:ind_event})
    return JsonResponse(response,safe=False)
