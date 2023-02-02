from .models import *

from django.shortcuts import redirect, render
from django.template import RequestContext

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
from django.views.generic.detail import DetailView, SingleObjectMixin

# Error Routes

# def bad_request(request):
#     # HTTP Error 400 Route
#     response = render_to_response(
#         'error.html', context_instance=RequestContext(request))
#     response.status_code = 400
#     return response


class About(TemplateView):
    # about route
    # info about the project, links, etc (TL;DR readme)
    template_name = 'about.html'


class AllClips(TemplateView):
    # home route / landing page
    # index route
    template_name = 'all_clips.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")
        if title != None:
            context['clips'] = Clip.objects.filter(title__icontains=title)
            context['header'] = f'Searching for {title}'
        else:
            context['clips'] = Clip.objects.all()
            context['tags'] = Tag.objects.all()
            context['header'] = 'Clip Collection Index'
        return context


class ClipDetail(DetailView):
    # clips/<clip.pk>
    # show / detail route for each Clip
    model = Clip
    template_name = 'clip_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class ClipCreate(LoginRequiredMixin, CreateView):
    # create route for Clip
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Clip
    fields = ['title', 'html', 'css', 'difficulty', 'tags']
    template_name = 'clip_create.html'

# validates form being submitted
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ClipCreate, self).form_valid(form)
# If successful, redirects user to the newly created Clip's detail page

    def get_success_url(self):
        print(self.kwargs)
        return reverse('clip_detail', kwargs={'pk': self.object.pk})


class ClipDelete(DeleteView):
    # delete route for each Clip
    # accessible via delete button on Clip Detail page
    # (only visible if user is authenticated / owner of that clip)
    model = Clip
    template_name = "clip_delete_confirmation.html"
    success_url = "/clips/"


@method_decorator(login_required, name='dispatch')
class ClipUpdate(UpdateView):
    # update / edit route for Clip
    # accessible via delete button on Clip Detail page
    # (only visible if user is authenticated / owner of that clip)
    model = Clip
    fields = ['title', 'html', 'css', 'difficulty', 'tags']
    template_name = 'clip_update.html'

    def get_success_url(self):
        # returns user to the Clip's detail page w/ the updated info
        return reverse_lazy('clip_detail', kwargs={'pk': self.object.pk})


class SignUp(View):
    # User Sign Up route
    # takes New User to sign up form page
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    # validates and submits the form
    # redirects User to the Clips Index page, with them signed in
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("all_clips")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


class Profile(TemplateView):
    # profile/<username>
    # route to view any user's profile
    model = Profile

    def get(self, request, username):
        try:
            user_data = User.objects.get(username=username)
            # get user data where username matches "username" param
            user_clips = Clip.objects.filter(owner=user_data.id)
            # get clips from db that are owned by that user
            print(user_data)
            print(user_clips)
        except User.DoesNotExist:
            return render(request, 'error.html', {'error_message': 'User not found'})

    # Render the template with the user data
        return render(request, 'profile.html', {'user_data': user_data, 'user_clips': user_clips})


class TagDetail(TemplateView):
    model = Tag
    template_name = 'tag_detail.html'

    # def list_posts_by_tag(request, tag_id):
    #     tag = get_object_or_404(Tag, id=tag_id)
    #     posts = Post.objects.filter(status="published", tags=tag)
    #     context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context['clips'] = Clip.objects.filter(tags__name=name)
            print('found tags')
        else:
            context['clips'] = None
            print('no tags found')
        print(context)
        return context
