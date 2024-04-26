from django import forms
from django.contrib.auth.models import User
from .models import Reservation,Passager,Trajet
from django.utils.timezone import now,datetime
class ReservationForm(forms.ModelForm):
    
    class Meta:
        model=Reservation
        fields=['num_reservation','num_place','trajet']
    def clean(self):
        today=now()
        t=Trajet.objects.filter(date_depart__gte=today)
        
        cleaned_data = super().clean()
        num_reservation=cleaned_data.get('num_reservation')
        num_place=cleaned_data.get('num_place')
        trajet=cleaned_data.get('trajet')
        if num_place<=0:
            self.add_error('num_place',"vous devez introduire un numéro de place valide")
        elif num_reservation<=0:
            self.add_error('num_reservation',"vous devez introduire un numéro de réservation valide")
        elif trajet not in t:
            self.add_error('trajet',"Ce trajet n'est plus valable")
class PassagerForm(forms.ModelForm):
    class Meta:
        model=Passager
        fields=['prénom','nom','date_de_naissance']
    def clean(self):
        cleaned_data=super().clean()
        prénom=cleaned_data.get('prénom')
        if any(char.isdigit() for char in prénom):
            self.add_error('prénom','le prénom ne doit pas contenir des chiffres')
        nom=cleaned_data.get('nom')
        if any(char.isdigit() for char in nom):
            self.add_error('nom','le nom ne doit pas contenir des chiffres')    
        
        