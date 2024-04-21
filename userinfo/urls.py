from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('userinfo/', userinfo, name='userinfo'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'),
         name='change_password'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
    path('delete_profile/', delete_profile, name='delete_profile'),
    # path('profile_deleted/', profile_deleted, name='profile_deleted'),
]
