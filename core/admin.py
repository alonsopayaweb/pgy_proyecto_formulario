from django.contrib import admin
from .models import Especie, Mascota

# Register your models here.
# Permite administrar el modelo completo

admin.site.register(Especie)
admin.site.register(Mascota)