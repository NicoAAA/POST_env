

""" 
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: POST (posts/models.py)
FECHA: 2024-08-01
VERSION: 4.5.6  
"""

# Importaciones de Django
from django.db import models

# Create your models here.

class Post(models.Model):
    '''
    CLASE Post.
    
    Esta clase define el modelo de la base de datos que se va a mostrar en la pagina de inicio de la aplicacion.
    
    args:
        models.Model: Clase de Django que se encarga de definir un modelo de la base de datos.
        
    Atributos:
        message: str
            Mensaje que se va a mostrar en la pagina de inicio.
            
    methods:
        __str__:
            Devuelve los primeros 50 caracteres del mensaje
    '''
    
    title = models.CharField(max_length=200) # Define el campo 'title' como un campo de caracteres con una longitud maxima de 200 caracteres.
    message = models.TextField() # Define el campo 'message' como un campo de texto.
    imagen= models.ImageField(upload_to='posts_images/', blank=True, null=True) # Define el campo 'imagen' como un campo de imagen.
    
    def __str__(self):
        return self.message[:50]
    