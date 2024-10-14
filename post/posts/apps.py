
""" 
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: POST (posts/apps.py)
FECHA: 2024-08-01
VERSION: 4.5.6  
"""

# Importaciones de Django
from django.apps import AppConfig


class PostsConfig(AppConfig):
    '''
    CONFIGURACION DE LA APLICACION DE POSTS.
    
    Esta clase se encarga de configurar la aplicacion de posts.
    
    args:
        AppConfig: Clase de Django que se encarga de configurar una aplicacion.
    
    Atributos:
        default_auto_field: str
        
            Define el tipo de campo que se va a utilizar por defecto en la base de datos.
        
        name: str
        
            Nombre de la aplicacion.
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
