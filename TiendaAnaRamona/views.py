from django.shortcuts import render, redirect
from django.urls import reverse
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

def hacer_pedido_vestido(request):
    if request.method == "POST":
        data = request.POST
        nombre = data["nombre"]
        color = data["color"]
        talle = data["talle"]
        vestido = Vestidos(nombre=nombre, talle=talle, color=color)
        vestido.save()
        

        url_exitosa = reverse('lista_vestidos')
        return redirect(url_exitosa)
    else:
        http_response = render(
            request=request,
            template_name="TiendaAnaRamona/formulario.html",
        )
        return http_response
    
def hacer_pedido_malla(request):
    if request.method == "POST":
        data = request.POST
        nombre = data["nombre"]
        color = data["color"]
        talle = data["talle"]
        malla = Malla(nombre=nombre, talle=talle, color=color)
        malla.save()
        

        url_exitosa = reverse('lista_mallas')
        return redirect(url_exitosa)
    else:
        http_response = render(
            request=request,
            template_name="TiendaAnaRamona/formulario_mallas.html",
        )
        return http_response
    
def hacer_pedido_sombrero(request):
    if request.method == "POST":
        data = request.POST
        nombre = data["nombre"]
        color = data["color"]
        talle = data["talle"]
        sombrero = Sombreros(nombre=nombre, talle=talle, color=color)
        sombrero.save()
        

        url_exitosa = reverse('lista_sombreros')
        return redirect(url_exitosa)
    else:
        http_response = render(
            request=request,
            template_name="TiendaAnaRamona/formulario_sombreros.html",
        )
        return http_response