from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import redirect

from functools import wraps

from datacenter.models import UserProfile
# Create your Own Role Check's

def allow_k12admin(view_func):
    def wrapper(request, *args, **kw):
        path = request.build_absolute_uri()
        full_path = request.get_full_path()
        user = request.user.profile.is_admin
        if not (user):
            return HttpResponse("<h1>You are not authorized person \
                                <a href='%s'>Click here to return home</a></h1>" %settings.LOGIN_REDIRECT_URL)
        else:
            return view_func(request, *args, **kw)
    return wrapper

def check_role_and_redirect(view_func):
    def wrapper(request, *args, **kw):
        path = request.build_absolute_uri()
        full_path = request.get_full_path()
        if request.user.profile.is_member:
            return redirect('/member/')
        elif request.user.profile.is_teacher:
            return redirect('/teacher/')
        elif request.user.profile.is_admin:
            return redirect('/admin/')
        else:
            return redirect('/signup/')
    return wrapper