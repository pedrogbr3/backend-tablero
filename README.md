# Tablero de Tareas

Proyecto para la Evaluacion 1 de Programacion Backend. El tema que me toco fue "Gestion de
Proyectos tipo Trello", asi que es un tablero simple con columnas y tareas (todavia no tiene
base de datos, eso queda para la proxima evaluacion).

Por ahora esto solo tiene la vista principal y una pagina de error 404, que era lo que pedia el
enunciado.

## Como correrlo

1. Clonar el repo
2. Crear el entorno virtual:

```
python3 -m venv .venv
```

3. Activarlo:

```
source .venv/bin/activate
```

(en Windows es `.venv\Scripts\activate`)

4. Instalar lo que pide requirements.txt:

```
pip install -r requirements.txt
```

5. Correr el servidor:

```
python manage.py runserver
```

6. Entrar a http://127.0.0.1:8000/

Si entran a una url que no existe, por ejemplo http://127.0.0.1:8000/asdasd, se deberia ver la
pagina de error 404 que hice.

## Como esta armado

- `backend/` es el proyecto (la config de Django)
- `tablero/` es la app, tiene la vista y las rutas
- `templates/` tiene el html de la vista principal y del 404

No use base de datos todavia, las columnas y tareas estan puestas directo en la vista
(`tablero/views.py`) para poder mostrar algo mientras no tengo el modelo hecho.
