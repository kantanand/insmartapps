from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

# Create your views here.
def index(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next_url' in request.get_full_path():
                url = request.get_full_path().split('=')[1]
            else:
                url = '/'
            return HttpResponseRedirect(url)
        else:
            form.data = form.data.copy()
            form.data['username'] = ''
            form.data['password'] = ''
            return render(request, 'common/login.html',locals())
    if request.method == 'GET':
        form_class = LoginForm
        context_dict = {
            'next_url' : settings.LOGIN_REDIRECT_URL,
            'LINKEDIN_API' : settings.LINKEDIN_API,
            'LINKEDIN_SUBMITTED_URL' : settings.LINKEDIN_SUBMITTED_URL,
            'LINKEDIN_IMAGE_URL' : settings.LINKEDIN_IMAGE_URL,
            'FACEBOOK_API' : settings.FACEBOOK_API,
            'GOOGLE_CLIENTID' : settings.GOOGLE_CLIENTID,
            'GOOGLE_REDIRECT' : settings.GOOGLE_REDIRECT,
            'FACEBOOK_SINGLE_URL' : settings.FACEBOOK_SINGLE_URL,
            'GOOGLE_SINGLE_URL' : settings.GOOGLE_SINGLE_URL,
            'LINKEDIN_SINGLE_URL' : settings.LINKEDIN_SINGLE_URL,
            'form':form_class
        }
        return render_to_response('common/login.html', context_dict, context_instance=RequestContext(request))

# ===============================================================
# Logout the user
# ===============================================================
def logout_user(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        logout(request)
    return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)