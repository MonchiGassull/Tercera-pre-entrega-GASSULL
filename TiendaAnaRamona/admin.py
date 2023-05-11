from django.contrib import admin

from TiendaAnaRamona.models import Vestidos, Sombreros, Malla, Comprador, Vendedor

# Register your models here.
admin.site.register(Vestidos)
admin.site.register(Sombreros)
admin.site.register(Malla)
admin.site.register(Comprador)
admin.site.register(Vendedor)