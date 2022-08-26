from django.contrib import admin

from InicioCabaña.models import Archivos, RegistroCabaña

# Register your models here.

class AdministrarRegistroCabaña(admin.ModelAdmin):
    list_display = ('nombre', 'costoDia', 'numPersonas')
    search_fields = ('nombre', 'costoDia', 'numPersonas')
    list_filter = ('nombre', 'costoDia', 'numPersonas')
    list_per_page = 10

admin.site.register(RegistroCabaña, AdministrarRegistroCabaña)

class AdministrarArchivos(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'comentario', 'archivo')
    search_fields = ('nombre', 'email', 'comentario', 'archivo')
    list_filter = ('nombre', 'email', 'comentario', 'archivo')
    list_per_page = 10

admin.site.register(Archivos, AdministrarArchivos)