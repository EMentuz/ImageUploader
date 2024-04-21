from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required


@login_required
def userinfo(request):
    return render(request, 'userinfo.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('userinfo')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        message = 'Профиль успешно удален'
        return render(request, 'delete_profile.html', {'message': message})
    return render(request, 'delete_profile.html')

# @login_required
# def delete_profile(request):
#     if request.method == 'POST':
#         user = request.user
#         user.delete()
#         return redirect('profile_deleted')
#     return render(request, 'delete_profile.html')

# def profile_deleted(request):
#     return render(request, 'profile_deleted.html')
