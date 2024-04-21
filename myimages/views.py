from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from app.models import Image
from myimages.forms import ChangeImageForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def myimages(request):
    user = request.user
    images = Image.objects.filter(user=user, is_deleted=False)
    return render(request, 'myimages.html', {'images': images})


@login_required
def my_image_detail(request, myimage_id):
    user = request.user
    # image = Image.objects.get(id=myimage_id, is_deleted=False, user=user,)
    image = get_object_or_404(Image, id=myimage_id, is_deleted=False, user=user)
    return render(request, 'myimage_detail.html', {'image': image})


@login_required
def change(request, myimage_id):
    user = request.user
    image = get_object_or_404(Image, pk=myimage_id, user=user)
    form = ChangeImageForm(request.POST or None, instance=image)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('myimages')

    return render(request, 'change.html', {'form': form, 'image': image})


def delete_image(request, myimage_id):
    if request.method == 'POST':
        image = Image.objects.get(pk=myimage_id)
        image.is_deleted = True
        image.deleted_at = timezone.now()
        image.save()
    return redirect('myimages')