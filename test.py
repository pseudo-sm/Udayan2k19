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

print(db.child("events").child("Civil").get().val())
