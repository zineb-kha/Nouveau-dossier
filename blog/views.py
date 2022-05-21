from django.shortcuts import render
from .models import Boitiers, Version, Fournisseur,Affectation, Carte_SIM, Véhicule
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from blog.forms import VersionForm, AffectationForm, FournisseurForm
from django.db.models import Q
from django.http import HttpResponseRedirect, FileResponse
import xlwt
import io 
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.contrib import messages

def home(request):
    notifications_count = 0
    notifications = []
    versions = Version.objects.all()

    form = AffectationForm
    if(request.method=='POST'):
        
        # hna bnshof eza kan geh tlab asln 
        form=AffectationForm(request.POST)
        form_data= (request.POST)

        if form.is_valid():
            # hna bnshof eza kan el tlb da mfhosh mshakl we bnfz el mtlob kolo
            form.save()
            boitier=Boitiers.objects.get(id=form_data["Nom_Boitier"])
            if boitier.is_taken==True:
                messages.info(request, "boitier is taken")
            boitier.is_taken=True
            boitier.save()
            véhicule=Véhicule.objects.get(id=form_data["Nom_Véhicule"])
            if véhicule.is_taken==True:
                messages.info(request, "véhicule is taken")
            véhicule.is_taken=True
            véhicule.save()
            sim=Carte_SIM.objects.get(id=form_data["Nom_SIM"])
            if sim.is_taken==True:
                messages.info(request, "boitier is taken")
            sim.is_taken=True
            sim.save()
        else:
            # hna lw el kan el tlb da fe mshakl fa bnwd7 eh el mshakl de kolha 
            boitier=Boitiers.objects.get(id=form_data["Nom_Boitier"])
            if boitier.is_taken==True:
                messages.info(request, "boitier is taken")
            # hna shofna eza kan el moshkla fe boitier fa b3tna massege ll template t2ol en el boitier feha moshkla
            véhicule=Véhicule.objects.get(id=form_data["Nom_Véhicule"])
            if véhicule.is_taken==True:
                messages.info(request, "véhicule is taken")
            # hna shofna eza kan el moshkla fe véhicule fa b3tna massege ll template t2ol en el véhicule feha moshkla
            
            sim=Carte_SIM.objects.get(id=form_data["Nom_SIM"])
            if sim.is_taken==True:
                messages.info(request, "boitier is taken")
            # hna shofna eza kan el moshkla fe sim fa b3tna massege ll template t2ol en el sim feha moshkla

    Version_form=VersionForm
    if(request.method=='POST'):
        Version_form=VersionForm(request.POST)
        if Version_form.is_valid():
            Version_form.save()

    Fournisseur_form=FournisseurForm
    if(request.method=='POST'):
        Fournisseur_form=FournisseurForm(request.POST)
        if Fournisseur_form.is_valid():
            Fournisseur_form.save()

    for version in versions:
        boitiers_count = Boitiers.objects.filter(is_taken=False , Version = version).count()
        if boitiers_count <= 2:
            notifications_count +=1
            notifications.append(f"Boitiers of version {version.Nom} are only {boitiers_count}")
    context={
        "notifications_count":notifications_count,
        "notifications":notifications,
        "form":form,
        "Version_form":Version_form,
        "Fournisseur_form":Fournisseur_form
    }
    return render(request,"index.html",context)

def search2(request):
    query=request.GET["Boitiers"]
    list_boitiers = Boitiers.objects.filter(Q(Numéro_boitier__contains=query) | Q(Version__Nom__contains=query) | 
    Q(Numéro_IMEM__contains=query) | Q(Fournisseur__Nom__contains=query))
    print(list_boitiers)
    return render(request,"search2.html",{"list_boitiers" : list_boitiers})

    


def SearchCarte_sim(request):
    query1=request.GET["Carte_SIM"]
    list_carte_sim = Carte_SIM.objects.filter(Q(Numéro_SIM__icontains = query1) | Q(Opérateur__icontains = query1))
    #list_carte_sim = Carte_SIM.objects.filter(Opérateur__icontains = query1)
    print (list_carte_sim)
    return render(request,"search1.html",{"list_carte_sim" : list_carte_sim})


def SearchVéhicule(request):
    query2=request.GET["Véhicule"]
    list_véhicule = Véhicule.objects.filter(Q(Nom__icontains = query2) | Q(Matricule__icontains = query2))
    #list_véhicule = Véhicule.objects.filter(Matricule__icontains = query2)
    print (list_véhicule)
    return render(request,"search3.html",{"list_véhicule" : list_véhicule})

def user_affectation(request):
    form=AffectationForm()
    if(request.method=='POST'):
        form=AffectationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')      #we are redirecting to the original page mark the actual url
        else:
            print(form.errors)
    list_affectation=Affectation.objects.all()
    return render(request,'index.html',{'list_affectation':list_affectation, 'form': form})

class add_affectation(CreateView):
     model=Affectation
     form_class=AffectationForm
     template_name="add-affect.html"
     success_url="index.html"

def user_version(request):
    form=VersionForm()
    if(request.method=='POST'):
        form=VersionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/my-admin/my-boitiers')      #we are redirecting to the original page mark the actual url
        else:
            print(form.errors)
    return render(request,'/my-admin/my-boitiers',{'form': form})

class AddVersion(CreateView):
     model=Version
     form_class=VersionForm
     template_name="add-version.html"
     success_url='/my-admin/my-boitiers'



class AddFournisseur(CreateView):
     model=Fournisseur
     form_class=FournisseurForm
     template_name="add-fournisseur.html"
     success_url='/my-admin/my-boitiers'


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['content-Disposition']= 'attachment; filename="AFFECTATION.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('AFFECTATION') 

    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold=True
    columns = ['Numéro_aff', 'Nom_Boitier', 'Numéro_boitier', 'Numéro_IMEM', 'Nom_SIM', 'Numéro_SIM', 'Nom_Véhicule', 'Matricule']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style= xlwt.XFStyle()

    rows = Affectation.objects.all()
    aa=('', '', '', 'Matricule')

    for row in rows:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num, row.Numéro_aff,row.Nom_Boitier,row.Nom_Boitierr.Numéro_boitier,
            row.Nom_Boitierr.Numéro_IMEM,
            row.Nom_SIM,
            row.Nom_SIM.Numéro_SIM,
            row.Nom_Véhicule,
            row.Nom_Véhicule.Matricule,
            row[col_num], font_style)
    
    wb.save(response)
    return response