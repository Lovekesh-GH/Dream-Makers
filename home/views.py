from django.shortcuts import render
from django.views.generic import TemplateView



def home(request):
    return render(request,"home.html")


def tasks(request):
    return render(request,"task.html")
