from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files import images
from django.db import IntegrityError

from .models import User, Profile, Upload

# Create your views here.
def index(request):
  
  return render(request, "index.html",{"home":True, "uploads":[upload for upload in Upload.objects.all()]})

def register(request):
  if request.method=="GET":
    if request.user.is_authenticated:
      return HttpResponseRedirect(reverse("index"))
    return render(request, "register.html",{"register":True})
  
  # This is needed to prepopulate the form with users data if there's any error
  message={}
  message["username"]=request.POST["username"]
  message["first_name"]=request.POST["first_name"]
  message["last_name"]=request.POST["last_name"]
  message["email"]=request.POST["email"]
  
  #check the image meet the required spec
  picture=request.FILES["picture"]
  img=images.ImageFile(picture)
  
  if img.height !=100 and img.width != 100:
    message["msg"]="only 100 by 100 px image accepted"
    return render(request, "register.html", message)
  try:
    #this will throw an error if not found
    User.objects.get(email=request.POST["email"])
    
    # A matching email is found 
    message["msg"]=f"{request.POST['email' ]} is associated with another account"
    return render(request,"register.html", message)
  except:
    pass
  
  
  try:
    
    user=User.objects.create_user(username=request.POST["username"].strip(), password=request.POST["password"])
    user.email=request.POST["email"]
    user.first_name=request.POST["first_name"]
    user.last_name=request.POST["last_name"]
    profile=Profile.objects.create(picture=request.FILES["picture"])
    user.profile=profile
    user.save()
    
    return render(request, "register.html", {"msg": "registration success please login","success": True})
  
  except IntegrityError:
    message["msg"]="username already taken"
    return render(request, "register.html", message)

@login_required
def profile(request):
  content={} 
  content["profile"]=True
  return render(request,"profile.html",content)

def login_view(request):
  if request.method == "GET":
    if request.user.is_authenticated:
      return HttpResponseRedirect(reverse("index"))
    return render(request, "login.html")
  
  password = request.POST["password"]
  username=request.POST["username"]
  
  user=authenticate(request, username=username, password=password)
  
  if user is not None:
   login(request, user)
   return HttpResponseRedirect(reverse('profile'))
  else:
   return render(request, "login.html", {"msg":"username or password incorrect ", "username":username})

@login_required
def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse("index"))

@login_required
def upload_view(request):
  if request.method=="GET": 
    return render(request, "upload.html", {"upload": True})
  
  pic=request.FILES["picture"]
  if str(pic).endswith(".png") or str(pic) .endswith(".jpg"):
    new_upload=Upload.objects.create(user=request.user, title=request.POST["title"])
    new_upload.description=request.POST["description"]
    new_upload.picture=request.FILES["picture"]
    new_upload.save()
    return render(request, "upload.html", {"upload":True, "msg":"uploaded successfully", "success":True})
  
  return render(request, "upload.html", {"upload":True, "msg":".png or .jpg required"})