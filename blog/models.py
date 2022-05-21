from django.db import models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

class Version(models.Model):
        Nom=models.CharField(max_length=50)

        def __str__(self):
                return self.Nom

class Fournisseur(models.Model):
        Nom=models.CharField(max_length=50)

        def __str__(self):
                return self.Nom

class Boitiers(models.Model):
        is_taken=models.BooleanField(default=False)
        user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
        Nom=models.CharField(max_length=50)
        Numéro_boitier=models.IntegerField()
        Numéro_IMEM=models.IntegerField()
        Version = models.ForeignKey(Version,on_delete=models.CASCADE , null=True ,blank=True,default=None)
        Fournisseur=models.ForeignKey(Fournisseur,on_delete=models.CASCADE , null=True,blank=True,default=None)
        Créé_le=models.DateTimeField(auto_now_add=True)
        Modifié_le=models.DateTimeField(auto_now=True)

        def __str__(self):
                return f"Name : {str(self.Nom)} Numéro_boitier : {str(self.Numéro_boitier)} Numéro_IMEM : {str(self.Numéro_IMEM)}"




class Carte_SIM(models.Model):
        is_taken=models.BooleanField(default=False)
        user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
        Nom=models.CharField(max_length=50)
        Numéro_SIM=models.IntegerField()
        Opérateur=models.CharField(max_length=35)
        Créé_le=models.DateTimeField(auto_now_add=True)
        Modifié_le=models.DateTimeField(auto_now=True)

        def __str__(self):
                return f"Name : {str(self.Nom)} Numéro_SIM : {str(self.Numéro_SIM)} Opérateur : {str(self.Opérateur)}"
        
        
        

class Véhicule(models.Model):
        is_taken=models.BooleanField(default=False)
        user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
        Nom=models.CharField(max_length=50)
        Matricule=models.CharField(max_length=50)
        Designation=models.CharField(max_length=35)
        Créé_le=models.DateTimeField(auto_now_add=True)
        Modifié_le=models.DateTimeField(auto_now=True)

        def __str__(self):
                return f"Name : {str(self.Nom)} Matricule : {str(self.Matricule)}" 

def get_absolute_url(self):
       return reverse("my-boitiers")           


class Affectation(models.Model):
        user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
        Numéro_aff= models.CharField(max_length=50)
        Nom_Boitier= models.OneToOneField(Boitiers,on_delete=models.CASCADE , null=True ,blank=True,default=None)
        Nom_SIM= models.OneToOneField(Carte_SIM,on_delete=models.CASCADE , null=True ,blank=True,default=None)
        Nom_Véhicule= models.OneToOneField(Véhicule,on_delete=models.CASCADE , null=True ,blank=True,default=None)

        def __str__(self):
                return self.Numéro_aff 

        
        