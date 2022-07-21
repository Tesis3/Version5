from django.urls import path
from productos.views import MarcaView, RubroView, SegmentoView, ProductoView

urlpatterns = [
    path('marca', MarcaView.as_view(), name='marca_list'),
    path('rubro', RubroView.as_view(), name='rubro_list'),
    path('segmento', SegmentoView.as_view(), name='segmento_list'),
    path('producto', ProductoView.as_view(), name='producto_list'),
]