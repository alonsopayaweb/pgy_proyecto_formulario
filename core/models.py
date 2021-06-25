from django.db import models


# Create your models here.

class Especie(models.Model):
    idEspecie = models.IntegerField(primary_key=True, unique=True, verbose_name='Id de especie')
    nombreEspecie =models.CharField(max_length=50, null=False, verbose_name='Nombre Especie')

    def __str__(self):
        return self.nombreEspecie

class Mascota(models.Model):
    chip = models.IntegerField(primary_key=True, blank=False, null=False, verbose_name='N° Chip')
    nombreMascota = models.CharField(max_length=20, null=False, default="", verbose_name='Nombre Mascota')
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, verbose_name='Especie')
    edad = models.PositiveSmallIntegerField()
    GENEROS = (('Macho', 'Macho'), ('Hembra', 'Hembra'))
    genero = models.CharField(max_length=6, choices=GENEROS, default='M')
    ESTERIL = (('Si', 'Si'), ('No', 'No'))
    esterilizado = models.CharField(max_length=2, choices=ESTERIL, default='S')
    imagen = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nombreMascota

    #Funcion para eliminar archivo de imagen
    def delete(self, *args, **kwargs):
        self.imagen.delete()
        super().delete(*args, **kwargs)


