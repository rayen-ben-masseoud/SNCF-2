from django.shortcuts import render
from django.utils.timezone import now
from django.http import HttpResponse
from .models import Trajet,Gare,Reservation,Passager
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request,id):
    ls=Gare.objects.get(id=id)
    
    return render(request,"main/trajets.html",{"ls":ls})
def home(request):
    return render(request,"main/home.html",{})
def trajets(request):
    today=now().date()
    g=Gare.objects.all()
    return render(request,"main/trajets.html",{"g":g,'today':today})
@login_required()
def reservations(request):
    
    r=Reservation.objects.filter(client=request.user)
    
    return render(request,"reservations/reservations.html",{'r':r})
def reservation(request,id):
    r=Reservation.objects.filter(client=request.user)
    rs=r.get(id=id)
    return render(request,"reservations/reservation.html",{'r':r,'rs':rs})
