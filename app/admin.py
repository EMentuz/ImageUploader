from django.contrib import admin
from .models import Image, Category
# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'uploaded_at', 'updated_at')
    list_filter = ('user', 'category', 'is_deleted')
    search_fields = ['id', 'description', 'category__name', 'user__username']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ['name']


