from django.shortcuts import render
from django.http import HttpResponse
from pyrebase import pyrebase
from django.contrib import auth



config = {
    'apiKey' : "AIzaSyDAr7Wnvd50LNabCTLf9wy2eceKg_S7Q2A",
    'authDomain' : "cpanel-2ed5d.firebaseapp.com",
    'databaseURL' : "https://cpanel-2ed5d.firebaseio.com",
    'projectId' : "cpanel-2ed5d",
    'storageBucket' : "",
    'messagingSenderId' : "694498267473",
    'appId' : "1:694498267473:web:64fc453e4d659d93408370",
    'measurementId' : "G-KC32DYYP6K"
  }

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()


def signIn(request):
    return render(request, 'harry/signIn.html')


def postsign(request):
      email=request.POST.get('email')
      passw=request.POST.get('pass')
      try:
         user= authe.sign_in_with_email_and_password(email,passw)
      except:
         message="Invalid Credentials"
         return render(request,'harry/signIn.html',{'mess':message})
      print(user)
      session_id=user['idToken']
      request.session['uid']=str(session_id)
      return render(request,'harry/welcome.html',{'e':email})
    
def logout(request):
  auth.logout(request)
  return render(request,'harry/signIn.html')