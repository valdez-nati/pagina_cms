from django.shortcuts import render, redirect
from .models import usuarios,noticias
import os
from pathlib import Path
from django.conf import settings
from .noticias import vern

def inicio(request):
        # Ordena las noticias por fecha de manera descendente
    noticias_ver = noticias.objects.filter(visible=True).order_by('fecha')
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
        noticias_con_imagen.append(noticia)
    context = {
        'contex': noticias_con_imagen,
    }
    return render(request, 'inicio.html',context)

def acceder(request):
    if request.method=='GET':
        if 'codigo_usuario' in request.session:
            #if request.session['codigo_usuario']>0:
                variables={}
                variables['nombre_usuario']= request.session['nombre_usuario']
                variables['nivel_usuario'] = request.session['nivel_usuario']
                print("Variable II",variables)
                return render(request, 'panel.html',variables)
        else:
            return render(request, 'acceder.html')
        
    if request.method=='POST':
        v_usuario=request.POST.get('usuario')
        v_clave=request.POST.get('clave')
        verificar_usuario= usuarios.objects.filter(usuario=v_usuario)
        variables={}
        if verificar_usuario.count()>0:
            if verificar_usuario[0].clave==v_clave:
                request.session['codigo_usuario']=verificar_usuario[0].id
                request.session['nombre_usuario']=verificar_usuario[0].nombre
                request.session['nivel_usuario']=verificar_usuario[0].nivel
                variables['nombre_usuario']= request.session['nombre_usuario']
                variables['nivel_usuario'] = request.session['nivel_usuario']
                print(request.session['nivel_usuario'])
                print("Variable",variables)
                return render(request, 'panel.html',variables)
            else:
                variables['m_error']='La contraseña es incorrecta'
                return render(request, 'acceder.html', variables)
        else:
                variables['m_error']='El usuario no existe'
                return render(request, 'acceder.html', variables)
        
def salir(request):
     # Eliminar toda la sesión del usuario
    request.session.flush()
    
    # Crear una respuesta de redirección
    response = redirect('inicio')
    
    # Añadir encabezados para evitar el caché
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate' # HTTP 1.1
    response['Pragma'] = 'no-cache' # HTTP 1.0
    response['Expires'] = '0' # Proxies
    
    return response