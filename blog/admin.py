from django.contrib import admin
from .models import Boitiers
from .models import Carte_SIM
from .models import Véhicule
from .models import Version
from .models import Fournisseur
from .models import Affectation

admin.site.register(Boitiers)
admin.site.register(Carte_SIM)
admin.site.register(Véhicule)
admin.site.register(Version)
admin.site.register(Fournisseur)
admin.site.register(Affectation)
