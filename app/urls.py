from .views import *
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', main, name='main'),
    path('register/', register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('image/<int:image_id>/', image_detail, name='image_detail'),
]
