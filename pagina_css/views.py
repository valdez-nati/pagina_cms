from django.shortcuts import render
from rest_framework import generics
from .serelizador import SerialNoticias, SerialDetalleNoticias,SerialUsuario,SerialComentarios,SerialGrupo
from .models import noticias, usuarios,comentarios,grupos


class NoticiasAPILista(generics.ListAPIView):
    queryset= noticias.objects.all()
    serializer_class=SerialNoticias




class NoticiasAPIDetalle(generics.RetrieveAPIView):
    lookup_field='id'
    queryset= noticias.objects.all()
    serializer_class= SerialDetalleNoticias

class UsuariAPILista(generics.ListAPIView):
    queryset= usuarios.objects.all()
    serializer_class=SerialUsuario


class ComentarioAPILista(generics.ListAPIView):
    queryset= comentarios.objects.all()
    serializer_class=SerialComentarios
    

class GruposAPILista(generics.ListAPIView):
    queryset= grupos.objects.all()
    serializer_class=SerialGrupo