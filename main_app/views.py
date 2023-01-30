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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")
        if title != None:
            context['clips'] = Clip.objects.filter(title__icontains=title)
            context['header'] = f'Searching for {title}'
        else:
            context['clips'] = Clip.objects.all()
            context['header'] = 'Clip Collection Index'
        return context


class ClipDetail(DetailView):
    model = Clip
    template_name = 'clip_detail.html'


class ClipCreate(CreateView):
    model = Clip
    fields = ['title', 'body', 'difficulty']
    template_name = 'clip_create.html'
    success_url = '/clips/'

# edit route
# delete route
