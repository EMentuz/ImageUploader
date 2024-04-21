# from django.contrib.auth.decorators import user_passes_test
# from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect


# def anonymous_required(function=None, redirect_url=None):
#    if not redirect_url:
#        redirect_url = settings.LOGIN_REDIRECT_URL
#
#    actual_decorator = user_passes_test(lambda u: u.is_anonymous(), login_url=redirect_url)
#
#    if function:
#        return actual_decorator(function)
#    return actual_decorator

def anonymous_required(view_func):
    """
    Декоратор, который ограничивает доступ к представлению только для анонимных пользователей.
    Если пользователь аутентифицирован, он будет перенаправлен на другую страницу.
    """
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Если пользователь аутентифицирован, перенаправляем его на другую страницу
            return redirect('main')  # Замените 'home' на URL вашей страницы
        else:
            # Если пользователь анонимен, позволяем ему получить доступ к представлению
            return view_func(request, *args, **kwargs)
    return wrapped_view