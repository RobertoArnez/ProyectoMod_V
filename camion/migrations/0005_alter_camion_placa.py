# Generated by Django 4.1.6 on 2023-02-18 15:23

import camion.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camion', '0004_alter_viaje_destino_alter_viaje_origen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camion',
            name='placa',
            field=models.CharField(max_length=7, validators=[camion.validators.validar_cuatro_cifras]),
        ),
    ]
