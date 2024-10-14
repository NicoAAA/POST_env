# post/admin.py

from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """
    Clase para personalizar la interfaz de administración del modelo Post.

    Atributos:
        list_display (tuple): Campos a mostrar en la lista de posts.
        fields (tuple): Campos a mostrar en el formulario de edición.
    """
    list_display = ('title', 'author', 'image')  # Campos a mostrar en la lista de posts
    fields = ('title', 'body', 'author', 'image')


# Register your models here.
admin.site.register(Post)


