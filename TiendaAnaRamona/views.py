from django.shortcuts import render

# Create your views here.

def lista_vestidos(request):
    contexto = {
        "vest" : [
            {"nombre": "Largo", "talle": "S" , "color": "Negro"},
            {"nombre": "Corto", "talle": "M" , "color": "Rojo"},
            {"nombre": "Largo", "talle": "L" , "color": "Beige"},
            {"nombre": "Corto", "talle": "XL" , "color": "Azul"},
        ]
    }
    http_response = render(
        
        request=request,
        template_name="TiendaAnaRamona/lista_vestidos.html",
        context=contexto,
    )
    return http_response

def lista_mallas(request):
    contexto = {
        "mall" : [
            {"nombre": "Enteriza", "talle": "S" , "color": "Negro"},
            {"nombre": "Enteriza", "talle": "M" , "color": "Rojo"},
            {"nombre": "Tankini", "talle": "L" , "color": "Verde Manzana"},
            {"nombre": "Tankini", "talle": "XL" , "color": "Azul"},
        ]
    }
    http_response = render(
        
        request=request,
        template_name="TiendaAnaRamona/lista_mallas.html",
        context=contexto,
    )
    return http_response

def lista_sombreros(request):
    contexto = {
        "somb" : [
            {"nombre": "Capelina", "talle": "S" , "color": "Blanco"},
            {"nombre": "Ala ancha", "talle": "M" , "color": "Beige"},
            {"nombre": "Ala ancha", "talle": "L" , "color": "Verde Militar"},
            {"nombre": "Capelina", "talle": "XL" , "color": "Azul"},
        ]
    }
    http_response = render(
        
        request=request,
        template_name="TiendaAnaRamona/lista_sombreros.html",
        context=contexto,
    )
    return http_response