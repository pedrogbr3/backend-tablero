-- Paso 3 de la Evaluacion 2: darle permisos al usuario de la aplicacion
-- solo sobre esta base de datos, no sobre todo el servidor.

GRANT ALL PRIVILEGES ON tablero_db.* TO 'tablero_user'@'%';
FLUSH PRIVILEGES;
