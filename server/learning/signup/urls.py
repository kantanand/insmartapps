from django.conf.urls import url
from signup import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ios_gurug/$', views.ios_gurug, name='ios_gurug'),
]