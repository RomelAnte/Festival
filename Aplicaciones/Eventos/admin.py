from django.contrib import admin
from .models import TipoUsuario, Usuario, Biografía, Festival, Presentacion, Entrada, Venta

# Register your models here.
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Biografía)
admin.site.register(Festival)
admin.site.register(Presentacion)
admin.site.register(Entrada)
admin.site.register(Venta)
