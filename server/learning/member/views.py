import datetime
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect

from common.decorators import check_role_and_redirect

# Create your views here.
def index(request):
    current_time = datetime.datetime.now()
    PAGE_TITLE = "Student Dashboard"
    LOGOUT_URL = settings.LOGOUT_URL
    return render(request,'member/dashboard.html',locals())