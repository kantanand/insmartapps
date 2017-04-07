from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^get-auth-token/', obtain_jwt_token),
]