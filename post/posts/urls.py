""" 
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: POST (posts/urls.py)
FECHA: 2024-08-01
VERSION: 4.5.6  
"""

"""
Este módulo define las rutas URL para la aplicación de posts.
Rutas:
- '' : Muestra la vista HomePageView y la nombra 'home'.
"""


# Importaciones de Django
from django.urls import path

# Importaciones locales
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home') # Define la ruta URL '' y la nombra 'home'.
]
