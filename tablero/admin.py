from django.contrib import admin

from .models import Tablero, Columna, Tarea

admin.site.register(Tablero)
admin.site.register(Columna)
admin.site.register(Tarea)
