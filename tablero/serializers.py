from rest_framework import serializers

from .models import Tablero, Columna, Tarea


class TableroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablero
        fields = '__all__'


class ColumnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Columna
        fields = '__all__'


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'
