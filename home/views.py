from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import LoginForm,RegistrationForm


def home(request):
    obj = LoginForm()
    obj1 = RegistrationForm()
    return render(request,"home.html",{"loginform":obj,"regform":obj1})


def tasks(request):
    return render(request,"task.html")
