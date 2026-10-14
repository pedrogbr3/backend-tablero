-- Paso 2 de la Evaluacion 2: crear el usuario que va a usar la aplicacion
-- (no el root).
--
-- OJO: aca se deja un placeholder en vez de una contraseña real, porque esto
-- se sube a un repositorio publico. Antes de correrlo, hay que reemplazar
-- 'CAMBIA_ESTA_CLAVE' por la misma clave que se puso en DB_PASSWORD del
-- archivo .env (que no se sube al repo).

CREATE USER IF NOT EXISTS 'tablero_user'@'%' IDENTIFIED BY 'CAMBIA_ESTA_CLAVE';
