from django.shortcuts import render


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
