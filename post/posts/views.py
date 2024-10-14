""" 
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: POST (posts/viws.py)
FECHA: 2024-08-01
VERSION: 4.5.6 

"""
#post/views.py

# Importaciones de Django
from django.shortcuts import render
from django.views.generic import ListView

# Importaciones locales 
from .models import Post

# Create your views here.
class HomePageView(ListView):
    
    model = Post
    template_name = "home.html"
    context_object_name = 'post_list'

