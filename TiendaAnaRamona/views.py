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

#cambiar a lista_mallas
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