from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from users.models import User


def home(req):
  return HttpResponse("<a href='/user/create'>Create</a><br/><a href='/user/login/'>Login</a>")


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
    

def login(req):
  return render(req, "user/login.html")


def loggedin(req):
  if req.method == "POST":
    uname = req.POST.get("uname")
    passwd = req.POST.get("pass")
    user = get_object_or_404(User, uname=uname, passwd=passwd)

    user = User(isloged=True)
    user.save()
    print("yönleniyor")
    return redirect(f"/{uname}/{passwd}")
  
  else:
    return redirect("/user/")
