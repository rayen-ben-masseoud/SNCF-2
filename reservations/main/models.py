from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Gare(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return "Gare "+self.name
class Trajet(models.Model):
    gare_depart=models.ForeignKey(Gare,on_delete=models.CASCADE,related_name="gare_depart")
    gare_arrivée=models.ForeignKey(Gare,on_delete=models.CASCADE,related_name="gare_arrivée")
    date_depart=models.DateTimeField(max_length=200)
    date_arrivée=models.DateTimeField(max_length=200)
    def __str__(self):
        depart=str(self.gare_depart)
        arrivee=str(self.gare_arrivée)
        date_dep=str(self.date_depart.day)+"/"+str(self.date_depart.month)+"/"+str(self.date_depart.year)+"-"+str(self.date_depart.hour)+"h"
        date_arr=str(self.date_arrivée.day)+"/"+str(self.date_arrivée.month)+"/"+str(self.date_arrivée.year)+"-"+str(self.date_arrivée.hour)+"h"
        return depart +"( "+ date_dep +" ) -> "+ arrivee + "( "+ date_arr+" )"
class Passager(models.Model):
    
    
    nom=models.CharField(max_length=200)
    prénom=models.CharField(max_length=200)
    date_de_naissance=models.DateField()
    def __str__(self):
        return self.prénom +" "+ self.nom 
class Reservation(models.Model):
    date_reservation=models.DateField(max_length=200)
    num_reservation=models.IntegerField()
    num_place=models.IntegerField()
    trajet=models.ForeignKey(Trajet,on_delete=models.CASCADE)
    passager=models.ForeignKey(Passager,on_delete=models.CASCADE)
    client=models.ForeignKey(User,on_delete=models.CASCADE)  
    def __str__(self):
        return "Réservation"+" "+str(self.passager) +" "+ str(self.num_reservation)


