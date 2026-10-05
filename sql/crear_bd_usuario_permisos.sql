-- Script SQL pedido en la Evaluacion 2: crear la base de datos, el usuario de
-- la aplicacion y sus permisos.
--
-- OJO: aca se deja un placeholder en vez de una contraseña real, porque esto
-- se sube a un repositorio publico. Antes de correrlo, hay que reemplazar
-- 'CAMBIA_ESTA_CLAVE' por la misma clave que se puso en DB_PASSWORD del
-- archivo .env (que no se sube al repo).

-- 1. Crear la base de datos
CREATE DATABASE IF NOT EXISTS tablero_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- 2. Crear el usuario que va a usar la aplicacion (no el root)
CREATE USER IF NOT EXISTS 'tablero_user'@'%' IDENTIFIED BY 'CAMBIA_ESTA_CLAVE';

-- 3. Darle permisos solo sobre esta base de datos, no sobre todo el servidor
GRANT ALL PRIVILEGES ON tablero_db.* TO 'tablero_user'@'%';

FLUSH PRIVILEGES;
