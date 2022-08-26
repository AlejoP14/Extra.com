# Generated by Django 4.1 on 2022-08-26 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InicioCabaña', '0006_alter_archivos_options_remove_archivos_comentario_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archivos',
            options={'ordering': ['-created'], 'verbose_name': 'Archivo', 'verbose_name_plural': 'Archivos'},
        ),
        migrations.RemoveField(
            model_name='archivos',
            name='CURP',
        ),
        migrations.RemoveField(
            model_name='archivos',
            name='Direccion',
        ),
        migrations.RemoveField(
            model_name='archivos',
            name='Edad',
        ),
        migrations.RemoveField(
            model_name='archivos',
            name='Medicamento',
        ),
        migrations.RemoveField(
            model_name='archivos',
            name='NombrePaciente',
        ),
        migrations.RemoveField(
            model_name='archivos',
            name='Sexo',
        ),
        migrations.RemoveField(
            model_name='archivos',
            name='Telefono',
        ),
        migrations.AddField(
            model_name='archivos',
            name='comentario',
            field=models.TextField(null=True, verbose_name='Comentario'),
        ),
        migrations.AddField(
            model_name='archivos',
            name='email',
            field=models.CharField(max_length=50, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='archivos',
            name='nombre',
            field=models.CharField(max_length=50, null=True, verbose_name='Nombre'),
        ),
    ]
