# Tablero de Tareas

Proyecto desarrollado para el ramo de Programacion Backend. El tema asignado corresponde a
"Gestion de Proyectos tipo Trello", por lo que la aplicacion representa un tablero con columnas
y tareas.

El proyecto se desarrollo en dos etapas:

- **Evaluacion 1**: estructura inicial del proyecto Django, con una vista de bienvenida y una
  pagina de error 404 personalizada. En esa etapa no existia modelo de datos ni persistencia.
- **Evaluacion 2** (etapa actual): se incorporo el modelo de datos (`Tablero`, `Columna`,
  `Tarea`), persistencia en MySQL, y una API REST completa con Django REST Framework
  (serializadores, `ModelViewSet` y rutas mediante `Router`), con operaciones CRUD completas.

La vista de bienvenida de la Evaluacion 1 se mantiene sin cambios, mostrando datos de ejemplo
fijos en el codigo. Los datos reales del tablero ahora se manejan a traves de la API.

## Requisitos

- Python 3.x
- Docker y Docker Compose (para levantar la base de datos MySQL)

## Instalacion y ejecucion

1. Clonar el repositorio.

2. Crear el entorno virtual y activarlo:

```
python3 -m venv .venv
source .venv/bin/activate
```

(en Windows: `.venv\Scripts\activate`)

3. Instalar las dependencias:

```
pip install -r requirements.txt
```

4. Crear el archivo `.env` a partir del ejemplo, y completar los valores propios:

```
cp .env.example .env
```

5. Levantar la base de datos MySQL (y phpMyAdmin) con Docker Compose:

```
docker compose up -d
```

La primera vez que se levanta el contenedor, MySQL ejecuta automaticamente el script
`sql/local/init.sql`, que crea la base de datos, el usuario de la aplicacion y sus permisos (ver
sección "Base de datos" mas abajo). phpMyAdmin queda disponible en
[http://localhost:8081](http://localhost:8081) para revisar las tablas de forma visual.

6. Aplicar las migraciones:

```
python manage.py migrate
```

7. Ejecutar el servidor:

```
python manage.py runserver
```

8. Acceder a http://127.0.0.1:8000/ para ver la vista de bienvenida, o a
   http://127.0.0.1:8000/api/ para ver la API REST.

Al ingresar a una URL inexistente (por ejemplo, http://127.0.0.1:8000/asdasd) se debe mostrar la
pagina de error 404 personalizada del proyecto.

## Base de datos

El script `sql/crear_bd_usuario_permisos.sql` contiene las instrucciones para crear la base de
datos, el usuario de la aplicacion y sus permisos. Por seguridad, ese script (que se sube al
repositorio) usa un **valor de ejemplo** en vez de una contraseña real.

Para uso local con Docker, existe una copia de ese mismo script con la contraseña real en
`sql/local/init.sql`. Ese archivo **no se sube al repositorio** (esta en `.gitignore`), y es el
que Docker Compose monta y ejecuta automaticamente al crear el contenedor por primera vez.

## Variables de entorno

Las credenciales y configuracion sensible (SECRET_KEY, datos de conexion a la base de datos) se
manejan mediante variables de entorno con la libreria `python-decouple`, y nunca quedan escritas
directamente en `settings.py`. El archivo `.env` con los valores reales no se sube al repositorio;
`.env.example` muestra que variables son necesarias, con valores de ejemplo.

## Endpoints de la API

Todos los endpoints se generan automaticamente mediante `ModelViewSet` y un `Router` de Django
REST Framework, y soportan el CRUD completo (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`):

- `/api/tableros/`
- `/api/columnas/`
- `/api/tareas/`

Cada uno tiene tambien su version de detalle (`/api/tareas/1/`, por ejemplo).

## Estructura del proyecto

- `backend/`: configuracion del proyecto Django (incluye lectura de variables de entorno).
- `tablero/`: aplicacion con el modelo de datos, serializadores, vistas (API y de bienvenida) y
  rutas.
- `templates/`: plantillas HTML de la vista de bienvenida y del error 404.
- `sql/`: scripts SQL de creacion de base de datos, usuario y permisos.
- `docker-compose.yml`: define los contenedores de MySQL y phpMyAdmin para desarrollo local.
