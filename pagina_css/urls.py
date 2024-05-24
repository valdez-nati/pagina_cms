from django.urls import path
from pagina_css import inicio, usuario, noticias, views, comentario
from django.conf import settings    
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('',inicio.inicio,name='inicio'),
    path('verusuario',usuario.ver,name='verusuario'),
    path('nueusuario',usuario.nuevo,name='nueusuario'),
    path('modusuario/<id>',usuario.modificar,name='modusuario'),
    path('borusuario/<id>_',usuario.borrar,name='borusuario'),
    path('acceder',inicio.acceder,name='acceder'),
    path('salir',inicio.salir,name='salir'),
    #------Noticias------------
    path('vernoticia',noticias.vern,name='vernoticia'),
    path('nuenoticia',noticias.nuevon,name='nuenoticia'),
    path('bornoticia/<id>_',noticias.borrarn,name='bornoticia'),
    path('modnoticia/<int:id>',noticias.modificarn,name='modnoticia'),

    #------Comentarios------------
    path('vercomen',comentario.verc,name='vercomen'),
    path('nuecomen',comentario.nuevoc,name='nuecomen'),
    
    #-----API-----------------------------
    path('listanoticias', views.NoticiasAPILista.as_view(), name='listanoticias'),
    path('listacomentarios', views.ComentarioAPILista.as_view(), name='listacomentarios'),
    path('listagrupos', views.GruposAPILista.as_view(), name='listagrupos'),

    path('listanoticias/<int:id>', views.NoticiasAPIDetalle.as_view(), name='detallenoticia'),
    #path('login/<int:id>', views.UsuariAPI.as_view(), name='login'),
    path('listausuarios', views.UsuariAPILista.as_view(), name='listausuarios'),
    path('admin/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

