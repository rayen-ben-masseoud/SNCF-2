from django.shortcuts import render,redirect,get_object_or_404
from django.utils.timezone import now
from django.http import HttpResponse
from .models import Trajet,Gare,Reservation,Passager
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
# Create your views here.
def index(request,id):
    ls=Gare.objects.get(id=id)
    
    return render(request,"main/trajets.html",{"ls":ls})
def home(request):
    return render(request,"main/home.html",{})
def trajets(request):
    today=now().date()
    g=Gare.objects.all()
    t=Trajet.objects.filter(date_depart__gte=today)
    return render(request,"main/trajets.html",{"g":g,'today':today,'t':t})
@login_required()
def reservations(request):
    
    r=Reservation.objects.filter(client=request.user)
    
    return render(request,"reservations/reservations.html",{'r':r})

@login_required()
def reservation(request,id):
    r=Reservation.objects.filter(client=request.user)
    rs=r.get(id=id)
    return render(request,"reservations/reservation.html",{'r':r,'rs':rs})


@login_required()
def edit_reservation(request,id=None):
    if id:
        reservation=get_object_or_404(Reservation,pk=id)
    else:
        reservation=None
    if request.method=='POST':
        form=ReservationForm(request.POST,instance=reservation)
        if form.is_valid():
            form.instance.client=request.user
            form.instance.date_reservation=now()
            reservation=form.save()
            if id:
                return redirect("reservation",id=id)
            else:
                
                return redirect("reservation",id=reservation.id)    
                
            
    
    else:
        form=ReservationForm(instance=reservation)
    return render(request,'reservations/nouvelle_reservation.html',{'form':form,'reservation':reservation})
@login_required()
def infos(request):
    client=request.user
    
    return render(request,"main/infos.html",{'c':client})  
    
