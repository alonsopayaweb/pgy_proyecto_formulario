# Generated by Django 3.2.3 on 2021-06-14 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='nombreMascota',
            field=models.CharField(default='', max_length=50, verbose_name='Nombre Mascota'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='nombreEspecie',
            field=models.CharField(max_length=50, verbose_name='Nombre Especie'),
        ),
    ]