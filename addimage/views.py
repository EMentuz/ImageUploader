from django.shortcuts import render, redirect
from addimage.forms import AddImageForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def add_image(request):
    if request.method == 'POST':
        form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)  # Создаем объект, но не сохраняем его в БД
            image.user = request.user  # Заполняем поле user текущим пользователем
            form.save()
            return render(request, 'add_image.html', {'message': 'Фото успешно добавлено'})
    else:
        form = AddImageForm()
    return render(request, 'add_image.html', {'form': form})