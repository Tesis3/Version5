from django.urls import path, include
from inicio.views import Inicio
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',Inicio.as_view(),name='inicio'),
    path('login/',auth_views.LoginView.as_view(template_name='inicio/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='inicio/login.html'),name='logout'),
]
