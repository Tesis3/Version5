from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from socios.models import Socio
from django.contrib.auth.mixins import LoginRequiredMixin
from socios.forms import SocioForm

# Create your views here.

class SociosView(LoginRequiredMixin, generic.ListView):
    model = Socio
    template_name = "socios/socios_list.html"
    context_object_name = "obj"
    login_url = 'inicio:login'

class SociosNuevo(generic.CreateView):
    model = Socio
    template_name = "socios/socios_form.html"
    context_object_name = "obj"
    form_class = SocioForm
    success_url = reverse_lazy("socios:socios_list")