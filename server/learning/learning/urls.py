"""learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

from login.views import logout_user

urlpatterns = patterns('',
    # Home Page
    # url(r'^$', home, name='home'),
    # admin --- urls
    url(r'^admin/', admin.site.urls),
    # login --- urls
    url(r'^login/', include('login.urls')),
    url(r'^logout/', logout_user, name='logout'),
    # signup --- urls
    url(r'^signup/', include('signup.urls', namespace='signup')),
)