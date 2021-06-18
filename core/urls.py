from django.urls import path
from .views import index, nosotros, gato, perro, contacto, donar, tablaMascotas, form_mascota, form_mod_mascota, form_del_mascota, form_ver_mascota, verMascota

urlpatterns = [
    path('', index, name="index"),
    path('nosotros', nosotros, name="nosotros"),
    path('gato', gato, name="gato"),
    path('perro', perro, name="perro"),
    path('contacto', contacto, name="contacto"),
    path('donar', donar, name="donar"),
    path('tablaMascotas', tablaMascotas, name="tablaMascotas"),
    path('form-mascota', form_mascota, name="form_mascota"),
    path('form-ver-mascota/<id>', form_ver_mascota, name="form_ver_mascota"),
    path('form-mod-mascota/<id>', form_mod_mascota, name="form_mod_mascota"),
    path('form-del-mascota/<id>', form_del_mascota, name="form_del_mascota"),
    path('verMascota/<id>', verMascota, name="verMascota"),
]