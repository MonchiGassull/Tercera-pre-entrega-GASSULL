"""
URL configuration for proyecto_prentrega3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyecto_prentrega3.views import saludar, saludar_con_html
from TiendaAnaRamona.views import lista_vestidos, lista_mallas, lista_sombreros, hacer_pedido_vestido, hacer_pedido_malla, hacer_pedido_sombrero

urlpatterns = [
    path("lista-vestidos/", lista_vestidos, name="lista_vestidos"),
    path("lista-mallas/", lista_mallas, name="lista_mallas"),
    path("lista-sombreros/", lista_sombreros, name="lista_sombreros"),
    path("pedido-vestido/", hacer_pedido_vestido, name="hacer_pedido_vestido"),
    path("pedido-malla/", hacer_pedido_malla, name="hacer_pedido_malla"),
    path("pedido-sombrero/", hacer_pedido_sombrero, name="hacer_pedido_sombrero"),
]
