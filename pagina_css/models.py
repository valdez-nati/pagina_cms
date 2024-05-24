from django.db import models

# Create your models here.
class grupos(models.Model):
    grupo  = models.CharField(max_length=45)
    
class usuarios(models.Model):
    nombre = models.CharField(max_length=20)
    usuario = models.CharField(max_length=20)
    clave = models.CharField(max_length=25)
    estado = models.CharField(max_length=25)
    nivel = models.CharField(max_length=25)
    
class noticias(models.Model):
    titudo = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now=True)
    cuerpo = models.CharField(max_length=3000)
    imagen = models.CharField(max_length=200)
    grupo = models.ForeignKey(grupos, on_delete=models.RESTRICT)
    autor = models.ForeignKey(usuarios, on_delete=models.RESTRICT)
    
class comentarios(models.Model):
    cuerpo = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now=True)
    visible = models.CharField(max_length=2, default='NO')
    autor = models.ForeignKey(usuarios, on_delete=models.RESTRICT)
    noticia = models.ForeignKey(noticias, on_delete=models.RESTRICT)