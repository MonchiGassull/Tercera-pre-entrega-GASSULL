from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def saludar(request, nombre):
    texto = f"Hola {nombre} bienvenido a nuestra tienda virtual de Ana Ramona"
    pagina_html = HttpResponse (texto)
    return pagina_html
