from datetime import timezone
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import comentarios,usuarios,grupos,noticias



def verc(request):
    if request.method=='GET':
        n_comen= comentarios.objects.all()  
        variables = {'request': request, 'n_comen': n_comen}
        print("Comentarios",variables)
        return render(request, 'ver_noticia.html', variables)


def nuevoc(request):
    
    if request.method=='POST':
        if 'codigo_usuario' in request.session and 'nivel_usuario' in request.session:
            nivel_usuario = request.session['nivel_usuario']
            usuario_f= request.session['codigo_usuario']
        
            print("Nivel de usuario:",nivel_usuario)
            print("id del grupo","Codigo usuario:",usuario_f)
            if nivel_usuario in ['ADMINISTRADOR', 'EDITOR','LECTOR']: 
                f_cuerpo = request.POST.get('cuerpo')
                f_fecha = request.POST.get('fecha')
                f_noticia = request.POST.get('noticia_id')
                noticia = noticias.objects.get(pk=f_noticia)
                autor_usuario = usuarios.objects.get(id=usuario_f)

                nuevocomem= comentarios(
                    cuerpo= f_cuerpo,
                    autor=autor_usuario,
                    noticia= noticia,
                )
                nuevocomem.save()
                # Verificar si el usuario es diferente de ADMINISTRADOR y EDITOR
                if nivel_usuario in ['EDITOR','LECTOR']:
                    messages.info(request, 'Su comentario está en revisión y será visible después de ser aprobado por un administrador ')

                return redirect('vernoticia')
    
def eliminar_comentario(request, id):
    if request.method == 'POST':
        comentario = get_object_or_404(comentarios, pk=id)
        noticia_id = comentario.noticia.id  # Guardar el ID de la noticia para redirigir después

        if 'codigo_usuario' in request.session and 'nivel_usuario' in request.session:
            usuario_f = request.session['codigo_usuario']
            nivel_usuario = request.session['nivel_usuario']

            if nivel_usuario in ['ADMINISTRADOR'] or comentario.autor.id == usuario_f:
                comentario.delete()
                messages.success(request, 'Comentario eliminado exitosamente.')
                return redirect('vernoticia')
            else:
                messages.error(request, 'No tiene permisos para eliminar este comentario.')
                return redirect('vernoticia')
        else:
            messages.error(request, 'Debe estar autenticado para eliminar un comentario.')

        return redirect('vernoticia', noticia_id=noticia_id)

    else:
        messages.error(request, 'Método no permitido.')
        return redirect('vernoticia', noticia_id=comentario.noticia.id)
    

def modcomen(request,id):
    comentario = get_object_or_404(comentarios, pk=id)
    if request.method=='POST':
       
        comentario.visible = request.POST.get('visible')
        
        comentario.save()
        return redirect('vernoticia')        
        
        