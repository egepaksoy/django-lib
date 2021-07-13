from django.shortcuts import render, HttpResponse, redirect
from users.models import User


def home(req):
  return HttpResponse("<a href='/user/create'>Create</a><br/><a href='/user/created/'>Created</a>")


def create(req):
  return render(req, "user/create.html")


def created(req):
  if req.method == "POST":
    uname = req.POST.get("uname")
    passwd = req.POST.get("pass")

    user = User(uname=uname, passwd=passwd)
    user.save()
    return redirect("/user/")
  
  if req.method == "GET":
    return redirect("/user/")
    
