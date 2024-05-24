from datetime import timezone
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.core.files.base import ContentFile
from .models import noticias,usuarios,grupos,comentarios
from django.conf import settings    
import os
from pathlib import Path

def vern(request):
    if request.method == 'GET':
        noticias_ver = noticias.objects.all()
        noticias_con_imagen = []

        for noticia in noticias_ver:
            if noticia.imagen and hasattr(noticia.imagen, 'path'):  # Verifica si noticia.imagen es válido y tiene el atributo 'path'
                imagen_path = os.path.join(settings.MEDIA_ROOT, str(noticia.imagen.path))
                if os.path.exists(imagen_path):
                    noticia.imagen_url = os.path.join(settings.MEDIA_URL, noticia.imagen.name)
                else:
                    noticia.imagen_url = None
            else:
                noticia.imagen_url = None  # Si noticia.imagen no es válido, establece None
            # Obtener comentarios asociados a la noticia
            noticia.comentarios = comentarios.objects.filter(noticia=noticia, visible='SI')
            noticias_con_imagen.append(noticia)

        context = {
            'contex': noticias_con_imagen,
        }
        return render(request, 'ver_noticia.html', context)

def nuevon(request):
    if request.method=='GET':
        n_grupos= grupos.objects.all()  
        variables = {'request': request, 'n_grupos': n_grupos}
        return render(request, 'noticia_nueva.html', variables)
    if request.method=='POST':
        if 'codigo_usuario' in request.session and 'nivel_usuario' in request.session:
            nivel_usuario = request.session['nivel_usuario']
            usuario_f= request.session['codigo_usuario']
           
            print("Nivel de usuario:",nivel_usuario)
            print("id del grupo","Codigo usuario:",usuario_f)
            if nivel_usuario in ['ADMINISTRADOR', 'EDITOR']: 
                f_titulo = request.POST.get('titulo')
                f_grupo = request.POST.get('grupo')
                f_cuerpo = request.POST.get('cuerpo')
                f_imagen = request.FILES.get('imagen')  # Usar get para manejar el caso de que el campo de imagen no esté presente
                autor_usuario = usuarios.objects.get(id=usuario_f)

                id_grupo = grupos.objects.get(id=f_grupo)
                print("id usuario",autor_usuario)
                ruta_imagen = 'imagenes/' + f_imagen.name
                with open(settings.MEDIA_ROOT / ruta_imagen, 'wb+') as destination:
                    for chunk in f_imagen.chunks():
                        destination.write(chunk)

                # Crear y guardar la nueva noticia
                nuevanoticia = noticias(
                    titudo=f_titulo,
                    cuerpo=f_cuerpo,
                   # fecha=timezone.now(),
                    imagen=f_imagen,
                    grupo=id_grupo,
                    autor=autor_usuario,
                )
                nuevanoticia.save()
                
                return redirect('vernoticia')
            else:
                # Manejar el caso de que no se haya proporcionado una imagen
                return render(request, 'noticia_nueva.html', {'error': 'Debe proporcionar una imagen'})


def borrarn(request, id):
    para_borrar =noticias.objects.get(pk=id)
    para_borrar.delete()
    return redirect('vernoticia')



def modificarn(request, id):

    noticia = get_object_or_404(noticias, pk=id)
    n_grupos = grupos.objects.all()
    print("Id de la noticia",noticia)
    # Si se envió un formulario con datos para actualizar el usuario
    if request.method == 'POST':
        f_titulo = request.POST.get('titulo')
        f_grupo_id = request.POST.get('grupo')
        f_cuerpo = request.POST.get('cuerpo')
        f_imagen = request.FILES.get('imagen')
        print("Current imagen value:", noticia.imagen)
        # Eliminar la imagen anterior si existe y se ha proporcionado una nueva imagen
        if f_imagen:
            if noticia.imagen :
                ruta_imagen_anterior = os.path.join(settings.MEDIA_ROOT, str(noticia.imagen.path))
                print("Ruta de la imagen anterior:", ruta_imagen_anterior)
                if os.path.exists(ruta_imagen_anterior):
                    os.remove(ruta_imagen_anterior)
                    print(f"Imagen anterior eliminada: {ruta_imagen_anterior}")

                ruta_imagen = 'imagenes/' + f_imagen.name
                ruta_imagen_completa = os.path.join(settings.MEDIA_ROOT, ruta_imagen)
                print(ruta_imagen_completa)
                with open(ruta_imagen_completa, 'wb+') as destination:
                    for chunk in f_imagen.chunks():
                        destination.write(chunk)
                noticia.imagen = f_imagen
        noticia.titudo = f_titulo
        noticia.grupo = get_object_or_404(grupos, pk=f_grupo_id)
        noticia.cuerpo = f_cuerpo
        noticia.save()

        return redirect('vernoticia')

    return render(request, 'noticia_mod.html', {'noticia': noticia, 'n_grupos': n_grupos})