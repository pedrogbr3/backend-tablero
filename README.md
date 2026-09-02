# Tablero de Tareas

Proyecto desarrollado para la Evaluacion 1 de Programacion Backend. El tema asignado corresponde
a "Gestion de Proyectos tipo Trello", por lo que la aplicacion representa un tablero con columnas
y tareas.

En esta etapa el proyecto no incluye modelo de datos ni persistencia en base de datos, ya que
dicho contenido corresponde a la siguiente evaluacion. Se implemento la vista principal y una
pagina de error 404 personalizada, conforme a lo solicitado en el enunciado.

## Instalacion y ejecucion

1. Clonar el repositorio.

2. Crear el entorno virtual:

```
python3 -m venv .venv
```

3. Activar el entorno virtual:

```
source .venv/bin/activate
```

(en Windows: `.venv\Scripts\activate`)

4. Instalar las dependencias:

```
pip install -r requirements.txt
```

5. Ejecutar el servidor:

```
python manage.py runserver
```

6. Acceder a http://127.0.0.1:8000/

Al ingresar a una URL inexistente (por ejemplo, http://127.0.0.1:8000/asdasd) se debe mostrar la
pagina de error 404 personalizada del proyecto.

## Estructura del proyecto

- `backend/`: configuracion del proyecto Django.
- `tablero/`: aplicacion que contiene la vista y las rutas.
- `templates/`: plantillas HTML de la vista principal y del error 404.

Las columnas y tareas se encuentran definidas directamente en la vista (`tablero/views.py`), dado
que el modelo de datos aun no ha sido implementado.
