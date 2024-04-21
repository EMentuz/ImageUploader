from django.shortcuts import render,  get_object_or_404
from .forms import UserRegistrationForm
from .models import Image, Category
from .decorators import anonymous_required


# Create your views here.
def main(request):
    images = Image.objects.filter(is_deleted=False).order_by('-uploaded_at')
    categories = Category.objects.all()

    # Обработка запроса для поиска и фильтрации
    search_query = request.GET.get('search')
    category_id = request.GET.get('category')

    if search_query:
        images = images.filter(description__iregex=search_query.lower())
    if category_id:
        images = images.filter(category_id=category_id)

    return render(request, 'main.html', {'images': images, 'categories': categories})


# @anonymous_required
# def login(request):
#     return render(request, 'login.html')


@anonymous_required
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'register_done.html', {'new_user': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': form})


def image_detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id, is_deleted=False)
    # image = Image.objects.get(id=image_id, is_deleted=False)
    return render(request, 'image_detail.html', {'image': image})
