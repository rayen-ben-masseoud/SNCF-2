from django import forms
from django.contrib.auth.models import User
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model=Reservation
        fields=['num_reservation','num_place','trajet','passager']
        