from datetime import timezone
from django.shortcuts import render,redirect,get_object_or_404
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
                
                return redirect('vernoticia')
    