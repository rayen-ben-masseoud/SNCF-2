from django.shortcuts import render
from django.http import HttpResponse
from .models import Trajet,Gare
# Create your views here.
def index(response,id):
    ls=Gare.objects.get(id=id)
    
    return render(response,"main/trajets.html",{"ls":ls})
def home(response):
    return render(response,"main/home.html",{})
def trajets(response):
    g=Gare.objects.all()
    return render(response,"main/trajets.html",{"g":g})