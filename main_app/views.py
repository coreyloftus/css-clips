from django.shortcuts import redirect
from django.http import HttpResponse

from .models import *
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'
