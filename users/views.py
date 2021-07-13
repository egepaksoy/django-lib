from django.shortcuts import render, HttpResponse


def create(req):
  return render(req, "user/create.html")