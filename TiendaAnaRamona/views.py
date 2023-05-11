from django.shortcuts import render
from TiendaAnaRamona.models import Malla, Sombreros, Vestidos, Comprador, Vendedor
# Create your views here.

def lista_vestidos(request):
    contexto = {
        "vest" : Vestidos.objects.all()
    }
    http_response = render(
        
        request=request,
        template_name="TiendaAnaRamona/lista_vestidos.html",
        context=contexto,
    )
    return http_response

def lista_mallas(request):
    contexto = {
        "mall" : Malla.objects.all()
    }
    http_response = render(
        
        request=request,
        template_name="TiendaAnaRamona/lista_mallas.html",
        context=contexto,
    )
    return http_response

def lista_sombreros(request):
    contexto = {
        "somb" : Sombreros.objects.all()
    }
    http_response = render(
        
        request=request,
        template_name="TiendaAnaRamona/lista_sombreros.html",
        context=contexto,
    )
    return http_response