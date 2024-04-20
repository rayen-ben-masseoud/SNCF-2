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
        return "Trajet "+str(self.gare_depart)+"("+str(self.date_depart.hour)+"h)"+"->"+str(self.gare_arrivée)+"("+str(self.date_arrivée.hour)+"h)"
   


