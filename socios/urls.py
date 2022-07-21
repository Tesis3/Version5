from django.urls import path
from socios.views import SociosView, SociosNuevo

urlpatterns = [
    path('socios', SociosView.as_view(), name='socios_list'),
    path('socios/nuevo',SociosNuevo.as_view(),name = 'socios_nuevo'),
]