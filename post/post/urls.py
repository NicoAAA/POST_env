"""
URL configuration for post project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

""" 
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: POST (post/urls.py)
FECHA: 2024-08-01
VERSION: 4.5.6  
"""

'''
Este módulo define las rutas URL para la aplicación de posts.

Rutas:
- 'admin/' : Muestra la vista de administrador de Django y la nombra 'admin'.
- '' : Incluye las rutas URL de la aplicación de posts.
'''

# Importaciones de Django para definir las rutas URL en modo de desarrollo:
from django.conf import settings

# Importaciones de Django para servir archivos de medios en modo de desarrollo:
from django.conf.urls.static import static

# Importaciones de Django para definir las rutas URL en admin:
from django.contrib import admin

# Importaciones de path y include para definir las rutas URL: 
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls), # Define la ruta URL 'admin/' y la nombra 'admin'.
    path('', include('posts.urls')), # Define la ruta URL '' y la nombra 'posts'.
]

if settings.DEBUG:  # Solo sirve archivos de medios en modo de desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
