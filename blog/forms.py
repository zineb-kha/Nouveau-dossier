from django import forms
from django.forms import ModelForm
from .models import Boitiers, Version, Fournisseur, Carte_SIM, Véhicule, Affectation

Frs = Fournisseur.objects.all().values_list('Nom','Nom')
choices = Version.objects.all().values_list('Nom','Nom')


class BoitierForm(forms.ModelForm):
    class Meta:
        model=Boitiers
        fields= ['Nom','Numéro_boitier','Numéro_IMEM','Version','Fournisseur']
        labels={'Nom':'Nom','Numéro_boitier':'Numéro_boitier','Numéro_IMEM':'Numéro_IMEM','Version':'Version',
        'Fournisseur':'Fournisseur'}
        widgets={
            'Nom':forms.TextInput(attrs={'class':'form-control'}),
            'Numéro_boitier':forms.TextInput(attrs={'class':'form-control'}),
            'Numéro_IMEM':forms.TextInput(attrs={'class':'form-control'}),
            'Version':forms.Select(choices=choices, attrs={'class':'form-control'}),
            'Fournisseur':forms.Select(choices=Frs, attrs={'class':'form-control'}),
        }


class Carte_simForm(forms.ModelForm):
    class Meta:
        model=Carte_SIM
        fields= ['Nom','Numéro_SIM','Opérateur']
        labels={'Nom':'Nom','Numéro_SIM':'Numéro_SIM','Opérateur':'Opérateur'}
        widgets={
            'Nom':forms.TextInput(attrs={'class':'form-control'}),
            'Numéro_SIM':forms.TextInput(attrs={'class':'form-control'}),
            'Opérateur':forms.TextInput(attrs={'class':'form-control'}),
        }


class VéhiculeForm(forms.ModelForm):
    class Meta:
        model=Véhicule
        fields= ['Nom','Matricule','Designation']
        labels={'Nom':'Nom','Matricule':'Matricule','Designation':'Designation'}
        widgets={
            'Nom':forms.TextInput(attrs={'class':'form-control'}),
            'Matricule':forms.TextInput(attrs={'class':'form-control'}),
            'Designation':forms.TextInput(attrs={'class':'form-control'}),
        }


class VersionForm(forms.ModelForm):
    class Meta:
        model=Version
        fields= ['Nom']
        labels={'Nom':'Nom'}
        widgets={
            'Nom':forms.TextInput(attrs={'class':'form-control'}),
        }


class FournisseurForm(forms.ModelForm):
    class Meta:
        model=Fournisseur
        fields= ['Nom']
        labels={'Nom':'Nom'}
        widgets={
            'Nom':forms.TextInput(attrs={'class':'form-control'}),
        }

class AffectationForm(forms.ModelForm):
    class Meta:
        model=Affectation
        fields= ['Numéro_aff','Nom_Boitier','Nom_SIM','Nom_Véhicule']
        labels={'Numéro_aff':'Numéro_aff','Nom_Boitier':'Nom_Boitier',
        'Nom_SIM':'Nom_SIM', 'Nom_Véhicule':'Nom_Véhicule' }
        widgets={
            'Numéro_aff':forms.TextInput(attrs={'class':'form-control'}),
            'Nom_Boitier':forms.Select(attrs={'class':'form-control'}),
            'Nom_SIM':forms.Select(choices=choices, attrs={'class':'form-control'}),
            'Nom_Véhicule':forms.Select(choices=Frs, attrs={'class':'form-control'}),
        }