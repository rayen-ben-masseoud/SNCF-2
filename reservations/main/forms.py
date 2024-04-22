from django import forms
from django.contrib.auth.models import User
from .models import Reservation,Passager

class ReservationForm(forms.ModelForm):
    class Meta:
        model=Reservation
        fields=['num_reservation','num_place','trajet']
 
class PassagerForm(forms.ModelForm):
    class Meta:
        model=Passager
        fields=['prénom','nom','date_de_naissance']
        