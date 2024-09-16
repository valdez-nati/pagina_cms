from rest_framework import generics
from .serelizador import SerialNoticias, SerialDetalleNoticias,SerialUsuario,SerialComentarios,SerialGrupo,NoticiasSerializer, GruposSerializer
from .models import noticias, usuarios,comentarios,grupos
from rest_framework import generics

#Retriew  para modificar 
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
    

class ComentariosAPINuevo(generics.CreateAPIView):
    queryset=comentarios.objects.all()
    serializer_class=SerialComentarios
    
class ComentariosAPIModificar(generics.RetrieveUpdateAPIView):
    lookup_field='id'
    queryset=comentarios.objects.all()
    serializer_class=SerialComentarios

class ComentariosAPIBorrar(generics.DestroyAPIView):
    lookup_field='id'
    queryset=comentarios.objects.all()