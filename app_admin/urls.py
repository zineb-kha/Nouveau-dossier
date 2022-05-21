from django.urls import path
from .views import *


urlpatterns=[
    path('',dashboard,name="dashboard"),
    path('my-boitiers',user_boitiers,name="my-boitiers"),
    path('ajouter-boitier',AddBoitier.as_view(),name="ajouter-boitier"),
    path('modifier-boitier/<int:pk>',UpdateBoitier.as_view(),name="modifier-boitier"),
    path('supprimer-boitier/<int:pk>',DeleteBoitier.as_view(),name="supprimer-boitier"),
    path('pdf-boitier',PdfBoitier,name="pdf-boitier"),


    path('my-carte_sim',user_carte_sim,name="my-carte_sim"),
    path('ajouter-carte_sim',AddCarte_sim.as_view(),name="ajouter-carte_sim"),
    path('modifier-carte_sim/<int:pk>',UpdateCarte_sim.as_view(),name="modifier-carte_sim"),
    path('supprimer-carte_sim/<int:pk>',DeleteCarte_sim.as_view(),name="supprimer-carte_sim"),

    path('my-véhicule',user_véhicule,name="my-véhicule"),
    path('ajouter-véhicule',AddVéhicule.as_view(),name="ajouter-véhicule"),
    path('modifier-véhicule/<int:pk>',UpdateVéhicule.as_view(),name="modifier-véhicule"),
    path('supprimer-véhicule/<int:pk>',DeleteVéhicule.as_view(),name="supprimer-véhicule"),

    path('ajouter-version',AddVersion.as_view(),name="ajouter-version"),

    path('ajouter-fournisseur',AddFournisseur.as_view(),name="ajouter-fournisseur"),


    path('my-affect',user_affectation,name="my-affect"),
    path('exel-affect',export_excel,name="exel-affect"),
    path('modifier-affect/<int:pk>',UpdateAffectation.as_view(),name="modifier-affect"),
    path('supprimer-affect/<int:pk>',DeleteAffectation.as_view(),name="supprimer-affect"),
    path("ajouter-affect",add_affectation,name="ajouter-affect"),
    path("boitier-count",boitier_count)
]