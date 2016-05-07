from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect

from common.decorators import check_role_and_redirect

# Create your views here.
@check_role_and_redirect
def index(request):
    return HttpResponse('signup page')