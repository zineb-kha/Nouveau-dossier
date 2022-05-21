from django.urls import path
from . import views

urlpatterns=[
      path("",views.home,name="home")
      path('my-affect',user_affectation,name="my-affect"),
      path('ajouter-version',AddVersion.as_view(),name="ajouter-version"),
      path('exel-affect',views.export_excel,name="exel-affect"),

      
      path('ajouter-version',AddVersion.as_view(),name="ajouter-version"),

      path('ajouter-fournisseur',AddFournisseur.as_view(),name="ajouter-fournisseur"),
]