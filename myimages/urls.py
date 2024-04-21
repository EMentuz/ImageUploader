from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('myimages/', myimages, name='myimages'),
    path('myimage/<int:myimage_id>/', my_image_detail, name='my_image_detail'),
    path('myimage/<int:myimage_id>/change/', change, name='change'),
    path('delete_image/<int:myimage_id>/', views.delete_image, name='delete_image'),

    # path('task/<int:task_id>/', task_detail, name='my_task_detail'),

]