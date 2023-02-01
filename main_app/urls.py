from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required, permission_required
from . import views

# add error routing in views.py
# from django.conf.urls import (handler400, handler403, handler404, handler500)
# handler400 = 'my_app.views.bad_request'
# handler403 = 'my_app.views.permission_denied'
# handler404 = 'my_app.views.page_not_found'
# handler500 = 'my_app.views.server_error'

urlpatterns = [
    path('', views.AllClips.as_view(), name="all_clips"),
    path('about/', views.About.as_view(), name='about'),
    path('clips/', views.AllClips.as_view(), name="all_clips"),
    path('clips/new', views.ClipCreate.as_view(), name="clip_create"),
    path('clips/<int:pk>', views.ClipDetail.as_view(), name="clip_detail"),
    path('clips/<int:pk>/delete', views.ClipDelete.as_view(), name="clip_delete"),
    path('clips/<int:pk>/update', views.ClipUpdate.as_view(), name="clip_update"),
    path('accounts/signup/', views.SignUp.as_view(), name="signup"),
    path('profile/<str:username>', views.Profile.as_view(), name="profile"),
    path('tags/<str:name>', views.TagDetail.as_view(), name="tag_detail")
]
