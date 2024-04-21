from django.urls import path
from .views import *

urlpatterns = [
    path('add_image/', add_image, name='add_image'),
]

