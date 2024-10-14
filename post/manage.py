#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

""" 
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: POST (post/manage.py)
FECHA: 2024-08-01
VERSION: 4.5.6  
"""
import os
import sys


def main():
    """Run administrative tasks."""
    
    '''
    FUNCION main.
    
    Esta funcion se encarga de ejecutar las tareas administrativas de Django.
    '''
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'post.settings') # Define la variable de entorno 'DJANGO_SETTINGS_MODULE' como 'post.settings'.
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc: # Importa la excepción 'ImportError' de Python.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc # Lanza la excepción 'ImportError'.
    execute_from_command_line(sys.argv) # Ejecuta las tareas administrativas de Django.


# Si el script se ejecuta directamente.
if __name__ == '__main__': 
    main()
