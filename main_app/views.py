from .models import *

from django.shortcuts import redirect, render

from django.http import HttpResponse
from django.urls import reverse_lazy, reverse

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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


# @method_decorator(login_required, name='dispatch')
# class AllClips(TemplateView):
#     template_name = 'all_clips.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         title = self.request.GET.get("title")
#         if title != None:
#             context['clips'] = User.objects.filter(
#                 title__icontains=title, user=self.request.user)
#             context['header'] = f'Searching for {title}'
#         else:
#             context['clips'] = Clip.objects.filter(user=self.request.user)
#             context['header'] = 'Clip Collection Index'
#         return context

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


class ClipCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Clip
    fields = ['title', 'html', 'css', 'difficulty']
    template_name = 'clip_create.html'
    # success_url = '/clips/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ClipCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('clip_detail', kwargs={'pk': self.object.pk})

# delete route


class ClipDelete(DeleteView):
    model = Clip
    template_name = "clip_delete_confirmation.html"
    success_url = "/clips/"

# edit route


@method_decorator(login_required, name='dispatch')
class ClipUpdate(UpdateView):
    model = Clip
    fields = ['title', 'html', 'css', 'difficulty']
    template_name = 'clip_update.html'

    def get_success_url(self):
        return reverse_lazy('clip_detail', kwargs={'pk': self.object.pk})
    # success_url = '/clips/'


class SignUp(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("all_clips")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
