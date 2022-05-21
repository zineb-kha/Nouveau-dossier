from django.shortcuts import render, redirect
from django.urls import include
from blog.models import Boitiers, Version, Fournisseur, Carte_SIM, Véhicule, Affectation
from blog.forms import BoitierForm, Carte_simForm, VéhiculeForm, VersionForm, FournisseurForm, AffectationForm
from django.views.generic.edit import UpdateView,CreateView,DeleteView, View
from django.db.models import Q
from django.http import HttpResponseRedirect, FileResponse, HttpResponse
import xlwt
import io 
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#Generate PDF

# PDF FOR LIST BOITIERS
def PdfBoitier(request):
    buf = io.BytesIO()

    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    
    list_boitiers=Boitiers.objects.all()
    lines = []

    for boitier in list_boitiers:

        textob.textLine("Nom:  %s" %(boitier.Nom))
        textob.textLine("Numéro_boitier:  %s" %(boitier.Numéro_boitier))
        textob.textLine("Numéro_IMEM:  %s" %(boitier.Numéro_IMEM))
        textob.textLine("Version: %s" %(boitier.Version))
        textob.textLine("Fournisseur:  %s" %(boitier.Fournisseur))
        #Other columns to be added
        textob.textLine(" ") 
        print(Boitiers,"\n")
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='boitier.pdf')

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

    rows = Affectation.objects.all().values_list('Numéro_aff', 'Nom_Boitier.Nom', 'Nom_SIM_id',
    'Nom_Véhicule')

    for row in rows:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    
    wb.save(response)
    return response

def dashboard(request):
    return render(request,'db.html')
    
# TABLE BOITIER

def user_boitiers(request):
    form=BoitierForm()
    if(request.method=='POST'):
        form=BoitierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-boitiers')      #we are redirecting to the original page mark the actual url
        else:
            print(form.errors)
    list_boitiers=Boitiers.objects.all()
    return render(request,'my-boitiers.html',{'list_boitiers':list_boitiers, 'form':form})

class AddBoitier(CreateView):
    model=Boitiers
    form_class=BoitierForm
    template_name="add-boitier.html"
    success_url="my-boitiers"

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    #def get_context_data(self, *args, **kwargs):    #Override this to add custom context data
        #context = super().get_context_data(*args, **kwargs)  # call super
        #context['form'] = self.form_class  # add to the returned dictionary
        #return context
     
class UpdateBoitier(UpdateView):
     model = Boitiers
     form_class = BoitierForm
     template_name ="app_admin/boitier_form.html"
     success_url='/my-admin/my-boitiers'

class DeleteBoitier(DeleteView):
    model = Boitiers
    success_url = "/my-admin/my-boitiers"

# TABLE VERSION

class AddVersion(CreateView):
     model=Version
     form_class=VersionForm
     template_name="add-version.html"
     success_url='/my-admin/my-boitiers'

# TABLE FOURNNISSEUR

class AddFournisseur(CreateView):
     model=Fournisseur
     form_class=FournisseurForm
     template_name="add-fournisseur.html"
     success_url='/my-admin/my-boitiers'
     
# TABLE CARTE_SIM

def user_carte_sim(request):
    form=Carte_simForm()
    if(request.method=='POST'):
        form=Carte_simForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-carte_sim')      #we are redirecting to the original page mark the actual url
        else:
            print(form.errors)
    list_carte_sim=Carte_SIM.objects.all()
    return render(request,'my-carte_sim.html',{'list_carte_sim':list_carte_sim, 'form':form})

class AddCarte_sim(CreateView):
     model=Carte_SIM
     form_class=Carte_simForm
     template_name="add-carte_sim.html"
     success_url="my-carte_sim"

class UpdateCarte_sim(UpdateView):
     model = Carte_SIM
     form_class = Carte_simForm
     template_name ="app_admin/carte_sim_form.html"
     success_url='/my-admin/my-carte_sim'

class DeleteCarte_sim(DeleteView):
    model = Carte_SIM
    success_url = "/my-admin/my-carte_sim"

# TABLE VEHICULE

def user_véhicule(request):
    form=VéhiculeForm()
    if(request.method=='POST'):
        form=VéhiculeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-véhicule')      #we are redirecting to the original page mark the actual url
        else:
            print(form.errors)
    list_véhicule=Véhicule.objects.all()
    return render(request,'my-véhicule.html',{'list_véhicule':list_véhicule,'form' : form})

class AddVéhicule(CreateView):
     model=Véhicule
     form_class=VéhiculeForm
     template_name="add-véhicule.html"
     success_url="my-véhicule"

class UpdateVéhicule(UpdateView):
     model = Véhicule
     form_class = VéhiculeForm
     template_name ="app_admin/véhicule_form.html"
     success_url='/my-admin/my-véhicule'

class DeleteVéhicule(DeleteView):
    model = Véhicule
    success_url = "/my-admin/my-véhicule"

# TABLE AFFECTATION

def user_affectation(request):
    form=AffectationForm()
    if(request.method=='POST'):
        form=AffectationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-affect')      #we are redirecting to the original page mark the actual url
        else:
            print(form.errors)
    list_affectation=Affectation.objects.all()
    return render(request,'my-affect.html',{'list_affectation':list_affectation, 'form': form})



def add_affectation(request):
    form = AffectationForm()
    if request.method=="POST":
        form = AffectationForm(request.POST)
        form_data= (request.POST)
        if form.is_valid():
            form.save()
            boitier=Boitiers.objects.get(id=form_data["Nom_Boitier"])
            print (boitier)
            boitier.is_taken=True
            boitier.save()
            véhicule=Véhicule.objects.get(id=form_data["Nom_Véhicule"])
            véhicule.is_taken=True
            véhicule.save()
            sim=Carte_SIM.objects.get(id=form_data["Nom_SIM"])
            sim.is_taken=True
            sim.save()
            return redirect("my-affect")

    context={
        "form":form
    }
    return render(request,'add-affect.html',context)

class UpdateAffectation(UpdateView):
     model = Affectation
     form_class = AffectationForm
     template_name ="app_admin/affect_form.html"
     success_url='/my-admin/my-affect'

class DeleteAffectation(DeleteView):
    model = Affectation
    success_url = "/my-admin/my-affect"


# SEARCH IN TABLE AFFECTATION

def search(request):
    query3=request.GET["Affectation"]
    list_affectations = Affectation.objects.filter(Q(Nom_Boitier__Nom__icontains=query3) | 
    Q(Nom_Boitier__Numéro_boitier__icontains=query3) | Q(Nom_Boitier__Version__Nom__icontains=query3) |
    Q(Nom_Boitier__Fournisseur__Nom__icontains=query3) | Q(Nom_SIM__Numéro_SIM__icontains=query3) |
    Q(Nom_SIM__Opérateur__icontains=query3) | Q(Nom_Véhicule__Nom__icontains=query3) | Q(Nom_Véhicule__Matricule__icontains=query3))

    print (list_affectations)
    return render(request,"search.html",{"list_affectations" : list_affectations})


#COUNT BOITIER

def boitier_count(request):
    boitiers = Boitiers.objects.filter(is_taken=False).count
    context={
        "boitiers":boitiers
    }
    return render(request,"boitiers_count.html",context)

#COUNT CARTE_SIM
