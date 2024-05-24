from django.shortcuts import render,redirect,get_object_or_404
from .models import usuarios


def ver(request):
    if request.method=='GET':
        if request.session['nivel_usuario']=='ADMINISTRADOR': #tiene que ser el administrador para ver las listas
            
            lista= usuarios.objects.all()
            variables={}
            variables['request']=request
            variables['lista']=lista
            
            return render(request, 'usuario_ver.html',variables)
        else:
            variables={}
            variables['m_error']='No tiene permisos para acceder'
            return render(request, 'panel.html', variables)
    else:
        return redirect('acceder')
def nuevo(request):
    if request.method=='GET':
        
        return render(request, 'usuario_nuevo.html')
    if request.method=='POST':
        f_nombre = request.POST.get('nombre')
        f_usuario = request.POST.get('usuario')
        f_clave=request.POST.get('clave')
        f_estado=request.POST.get('estado')
        f_nivel=request.POST.get('nivel')
        # en donde esta la tabla el boton de nuevo usuario
        nuevousuario=usuarios(
            nombre=f_nombre,
            usuario = f_usuario,
            clave = f_clave,
            estado = f_estado,
            nivel = f_nivel
            #los datos del formulario que se trajo
        )
        nuevousuario.save()#para guardar en la base de datos 
        return redirect('verusuario')
    

    
def modificar(request, id):
    usuario = get_object_or_404(usuarios, pk=id)
    
    # Si se envió un formulario con datos para actualizar el usuario
    if request.method == 'POST':
        # Actualizar los campos del usuario con los datos enviados en la solicitud
        usuario.nombre = request.POST.get('nombre')
        usuario.usuario = request.POST.get('usuario')
        usuario.clave = request.POST.get('clave')
        usuario.estado = request.POST.get('estado')
        usuario.nivel = request.POST.get('nivel')
        usuario.save()  # Guardar los cambios en la base de datos
        return redirect('verusuario')  # Redireccionar a la página de lista de usuarios
    
    # Si la solicitud es GET, renderizar el formulario de modificación con los datos del usuario
    return render(request, 'usuario_mod.html', {'usuario': usuario})

def borrar(request, id):
    para_borrar =usuarios.objects.get(pk=id)
    para_borrar.delete()
    return redirect('verusuario')


