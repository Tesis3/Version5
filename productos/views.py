from django.shortcuts import render
from django.views import generic
from productos.models import Marca, Rubro, Segmento, Producto
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = "productos/marca_list.html"
    context_object_name = "obj"
    login_url = 'inicio:login'

class RubroView(LoginRequiredMixin, generic.ListView):
    model = Rubro
    template_name = "productos/rubro_list.html"
    context_object_name = "obj"
    login_url = 'inicio:login'

class SegmentoView(LoginRequiredMixin, generic.ListView):
    model = Segmento
    template_name = "productos/segmento_list.html"
    context_object_name = "obj"    
    login_url = 'inicio:login'    

class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "productos/producto_list.html"
    context_object_name = "obj"
    login_url = 'inicio:login'            