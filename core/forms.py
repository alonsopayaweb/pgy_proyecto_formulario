from django import forms    
from django.forms import ModelForm
from .models import Mascota
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Definimos formulario de registro
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario', widget= forms.TextInput(attrs={'placeholder':'Ingrese Nombre de Usuario'}))
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder':'usuario@ejemplo.com'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'placeholder':'********'}))
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput(attrs={'placeholder':'********'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #Para iterar campos de ayuda y eliminarlos por defecto
        help_texts = {k:"" for k in fields }

#Definimos formulario para mascota
class MascotaForm(ModelForm):

    #Definimos validaciones de caracteres minimos y maximos y placeholders
    chip = forms.CharField(min_length =  5, max_length = 10, label='N° Chip', widget= forms.TextInput(attrs={'placeholder':'Ingrese N° Chip'}))
    nombreMascota = forms.CharField(min_length = 3, max_length=20, label="Nombre Mascota", widget= forms.TextInput(attrs={'placeholder':'Ingrese Nombre'}))
    edad = forms.IntegerField(min_value = 1, max_value = 20, label="Edad", widget= forms.NumberInput(attrs={'placeholder':'Ingrese Edad'}))

    class Meta:
        model = Mascota
        fields = ['chip','nombreMascota','especie','edad','genero','esterilizado','imagen']

    #Definimos un placeholder para el campo de especie
    def __init__(self, *args, **kwargs): 
        super(MascotaForm, self).__init__(*args, **kwargs) 
        self.fields['especie'].empty_label = "Seleccione una Especie"
        