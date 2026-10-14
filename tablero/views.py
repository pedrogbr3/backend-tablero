from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Tablero, Columna, Tarea
from .serializers import TableroSerializer, ColumnaSerializer, TareaSerializer


def inicio(request):
    nombre_proyecto = "Tablero de Tareas"

    columnas = [
        {"titulo": "Por hacer", "tareas": ["Diseñar la base de datos", "Revisar apuntes de Django"]},
        {"titulo": "Haciendo", "tareas": ["Terminar la vista principal"]},
        {"titulo": "Listo", "tareas": ["Instalar Django", "Crear el entorno virtual", "Crear el repositorio"]},
    ]

    # voy sumando el total de tareas y guardo cuantas tiene cada columna
    total = 0
    for col in columnas:
        cant = len(col["tareas"])
        col["cantidad"] = cant
        total = total + cant
        if cant == 0:
            col["mensaje"] = "No hay tareas aca todavia"
        else:
            col["mensaje"] = ""

    if total == 0:
        estado = "El tablero esta vacio"
    elif total < 5:
        estado = "Recien empezando"
    else:
        estado = "Hay harto trabajo"

    contexto = {
        "nombre_proyecto": nombre_proyecto,
        "columnas": columnas,
        "total": total,
        "estado": estado,
    }
    return render(request, "tablero/inicio.html", contexto)


# a partir de aca, lo nuevo de la Evaluacion 2: un ModelViewSet por cada
# modelo, para tener el CRUD completo (GET, POST, PUT, PATCH, DELETE) sin
# tener que escribir cada vista a mano

class TableroViewSet(viewsets.ModelViewSet):
    queryset = Tablero.objects.all()
    serializer_class = TableroSerializer


class ColumnaViewSet(viewsets.ModelViewSet):
    queryset = Columna.objects.all()
    serializer_class = ColumnaSerializer


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer


# a partir de aca, lo nuevo de la Evaluacion 3: autenticacion y vistas
# protegidas, una basada en funcion y otra basada en clase.

@login_required
def panel_funcion(request):
    contexto = {
        "cantidad_tableros": Tablero.objects.count(),
        "cantidad_columnas": Columna.objects.count(),
        "cantidad_tareas": Tarea.objects.count(),
    }
    return render(request, "tablero/panel_funcion.html", contexto)


class PanelClaseView(LoginRequiredMixin, TemplateView):
    template_name = "tablero/panel_clase.html"
    # si no esta logueado, LoginRequiredMixin lo manda solo a LOGIN_URL

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["cantidad_tableros"] = Tablero.objects.count()
        contexto["cantidad_columnas"] = Columna.objects.count()
        contexto["cantidad_tareas"] = Tarea.objects.count()
        return contexto
