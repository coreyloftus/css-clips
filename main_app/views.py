from django.shortcuts import redirect
from django.http import HttpResponse

from .models import *
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


class AllClips(TemplateView):
    template_name = 'all_clips.html'


class ClipDetail(DetailView):
    model = Clip
    template_name = 'clip_detail.html'


class ClipCreate(CreateView):
    model = Clip
    fields = ['title', 'body', 'difficulty']
    template_name = 'clip_create.html'
    success_url = '/clips/'
