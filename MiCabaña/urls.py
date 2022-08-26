"""MiCabaña URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from distutils.debug import DEBUG
from django.contrib import admin
from django.urls import path
from InicioCabaña import views
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('comentarios/', views.comentarios, name='comentarios'),
    path('archivos/', views.archivos, name='Subir'),
    path('consultasSQL/', views.consultasSQL, name='consultasSQL'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('consultarComentario/<int:id>', views.consultarComentario, name='consultarComentario'),
    path('editarComentario/<int:id>', views.editarComentario, name='editarComentario'),
    
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)