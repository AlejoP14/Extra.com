

from django.db import models

my_chosens = (
    ('Si', 'Si'),
    ('No', 'No'),
)

class RegistroCabaña(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Clave')
    oferta = models.CharField(max_length=2, choices=my_chosens, default='No', verbose_name='Oferta')
    nombre = models.CharField(max_length=50, verbose_name='Titulo')
    descripcion = models.TextField(null=True ,verbose_name='Descripcion')
    costoDia = models.IntegerField(verbose_name='Costo por dia')
    numPersonas = models.IntegerField(verbose_name='Numero de personas')
    numCamas = models.IntegerField(verbose_name='Numero de camas')
    lugar = models.CharField(max_length=50, verbose_name='Lugar')
    imagen = models.ImageField(upload_to='Imagenes', null=True, blank=True)
    Cocina = models.CharField(null=True, max_length=50, choices=my_chosens ,verbose_name='Cocina')
    Baño = models.CharField(max_length=10, choices=my_chosens, verbose_name='Baño')
    Wifi = models.CharField(max_length=10, choices=my_chosens, verbose_name='Wifi')
    Telefono = models.CharField(max_length=10, choices=my_chosens, verbose_name='Telefono')
    Televisor = models.CharField(max_length=10, choices=my_chosens, verbose_name='Televisor')
    Botiquin = models.CharField(max_length=10, choices=my_chosens, verbose_name='Botiquin')
    Calefaccion = models.CharField(max_length=10, choices=my_chosens, verbose_name='Calefaccion')
    Extinguidor = models.CharField(max_length=10, choices=my_chosens, verbose_name='Extinguidor')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    class Meta:
        verbose_name = 'Registro de Cabañas'
        verbose_name_plural = 'Registro de Cabañas'
        ordering = ['id']
    def __str__(self):
        return self.nombre
    
class Archivos(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombre = models.CharField(null=True, max_length=50, verbose_name="Nombre")
    email = models.CharField(null=True, max_length=50, verbose_name="Email") 
    comentario = models.TextField(null=True, verbose_name="Comentario")
    archivo = models.FileField(upload_to="archivos", null=True, blank=True, verbose_name="Identificacion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
        ordering = ["-created"]
        
        def __str__(self):
            return self.archivo