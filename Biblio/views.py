from django.shortcuts import render
from django.views.generic import TemplateView
from Biblio.models import *

# Create your views here.

class HomeView(TemplateView):
    template_name = 'Biblio/home.html'
    