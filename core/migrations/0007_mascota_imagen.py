# Generated by Django 3.2.3 on 2021-06-16 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_mascota_chip'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
