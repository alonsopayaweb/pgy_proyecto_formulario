from django import forms    
from django.forms import ModelForm
from .models import Mascota

class MascotaForm(ModelForm):

    class Meta:
        model = Mascota
        fields = ['chip','nombreMascota','especie','edad','genero','esterilizado','imagen']

        