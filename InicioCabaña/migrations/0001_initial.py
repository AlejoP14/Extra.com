# Generated by Django 4.1 on 2022-08-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroCabaña',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('nombre', models.CharField(max_length=50, verbose_name='Titulo')),
                ('costoDia', models.IntegerField(verbose_name='Costo por dia')),
                ('numPersonas', models.IntegerField(verbose_name='Numero de personas')),
                ('numCamas', models.IntegerField(verbose_name='Numero de camas')),
                ('lugar', models.CharField(max_length=50, verbose_name='Lugar')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='Imagenes')),
                ('Cocina', models.BooleanField(default=False, verbose_name='Cocina')),
                ('Baño', models.BooleanField(default=False, verbose_name='Baño')),
                ('Wifi', models.BooleanField(default=False, verbose_name='Wifi')),
                ('Telefono', models.BooleanField(default=False, verbose_name='Telefono')),
                ('Televisor', models.BooleanField(default=False, verbose_name='Televisor')),
                ('Botiquin', models.BooleanField(default=False, verbose_name='Botiquin')),
                ('Calefaccion', models.BooleanField(default=False, verbose_name='Calefaccion')),
                ('Extinguidor', models.BooleanField(default=False, verbose_name='Extinguidor')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Registro de Cabañas',
                'verbose_name_plural': 'Registro de Cabañas',
                'ordering': ['id'],
            },
        ),
    ]
