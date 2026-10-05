from django.db import models


class Tablero(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Columna(models.Model):
    tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE, related_name='columnas')
    nombre = models.CharField(max_length=100)
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} ({self.tablero.nombre})"


class Tarea(models.Model):
    columna = models.ForeignKey(Columna, on_delete=models.CASCADE, related_name='tareas')
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
