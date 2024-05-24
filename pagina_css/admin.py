from django.contrib import admin
from .models import usuarios,noticias, grupos, comentarios
# Register your models here.

admin.site.register(usuarios)
admin.site.register(noticias)
admin.site.register(grupos)
admin.site.register(comentarios)