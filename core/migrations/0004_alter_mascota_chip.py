# Generated by Django 3.2.3 on 2021-06-15 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_mascota_esterilizado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='chip',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Id de Mascota'),
        ),
    ]
