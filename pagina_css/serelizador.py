from rest_framework import serializers
from .models import noticias,usuarios,comentarios,grupos

class SerialNoticias(serializers.ModelSerializer):
    class Meta:
        model= noticias
        fields = [
            'id',
            'titudo',
            'fecha',
            'cuerpo',
            'imagen',
            'autor',
        ]
        
class SerialDetalleNoticias(serializers.ModelSerializer):
    class Meta:
        model = noticias
        fields=[
            'id',
            'titudo',
            'fecha',
            'cuerpo',
            'imagen',
            'autor',
        ]

class SerialUsuario(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields=[
            'id',
            'nombre',
            'usuario',
            'clave',
            'estado',
            'nivel',
        ]

class SerialComentarios(serializers.ModelSerializer):
    class Meta:
        model = comentarios
        fields=[
            'id',
            'cuerpo',
            'fecha',
            'visible',
            'autor',
            'noticia',
        ]

class SerialGrupo(serializers.ModelSerializer):
    class Meta:
        model = grupos
        fields=[
            'id',
            'grupo',
        ]


class NoticiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = noticias
        fields = '__all__'

class GruposSerializer(serializers.ModelSerializer):
    class Meta:
        model = grupos
        fields = '__all__'