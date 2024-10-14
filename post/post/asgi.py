"""
ASGI config for post project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

""" 
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: POST (posts/asgi.py)
FECHA: 2024-08-01
VERSION: 4.5.6  
"""

import os # Importa el modulo 'os' de Python.

from django.core.asgi import get_asgi_application # Importa la función 'get_asgi_application' del modulo 'django.core.asgi'.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'post.settings') # Define la variable de entorno 'DJANGO_SETTINGS_MODULE' como 'post.settings'.

application = get_asgi_application() # Define la aplicación ASGI como 'application'.
