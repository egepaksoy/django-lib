from django.urls import path
from . import views


urlpatterns = [
  path('', views.home),
  path('create/', views.create),
  path('created/', views.created),
]
