from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Inicio(LoginRequiredMixin, generic.TemplateView):
    template_name = 'base/base.html'
    login_url = 'inicio:login'