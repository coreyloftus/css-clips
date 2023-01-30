from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'

# index route


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

# show route


class ClipDetail(DetailView):
    model = Clip
    template_name = 'clip_detail.html'

    def detail_view(request, item_id):
        clip = Clip.objects.get(id=item_id)
        return render(request, 'clip_live.html', {'clip': clip})

# create route


class ClipCreate(CreateView):
    model = Clip
    fields = ['title', 'html', 'css', 'difficulty']
    template_name = 'clip_create.html'
    success_url = '/clips/'

# delete route


class ClipDelete(DeleteView):
    model = Clip
    template_name = "clip_delete_confirmation.html"
    success_url = "/clips/"

# edit route


class ClipUpdate(UpdateView):
    model = Clip
    fields = ['title', 'html', 'css', 'difficulty']
    template_name = 'clip_update.html'

    def get_success_url(self):
        return reverse_lazy('clip_detail', kwargs={'pk': self.object.pk})
    # success_url = '/clips/'
