from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Create your views here.
def index(request):
    return HttpResponse('signup page')

@api_view(['POST'])
@permission_classes((AllowAny,))
def ios_gurug(request):
    '''
    User Registration from ios gurug app
    '''
    if request.method == 'POST':
        user_name = request.POST['username']
        user_passord = request.POST['user_password']
        first_name = request.POST.get('first_name', 'Kantanand')
        last_name = request.POST.get('last_name', 'US')
        user, is_new_user = User.objects.get_or_create(username=user_name)
        if is_new_user:
            user.first_name = first_name
            user.last_name = last_name
            user.email = user_name
            user.is_active = True
            user.is_staff = True
            user.set_password(user_passord)
            user.save()
            user_profile = user.profile
            user_profile.first_name = first_name
            user_profile.last_name = last_name
            user_profile.email = user.username
            user_profile.save()
            result_dict = {
                'token': 'some token going to be sent like jwt_token',
                'status': True,
                'is_new_user': is_new_user,
                'username': user.username
            }
            return Response(result_dict, status=200)
        elif user.is_active:
            result_dict = {
                'token': 'some token going to be sent like jwt_token',
                'status': True,
                'is_new_user': is_new_user,
                'username': user.username
            }
            return Response(result_dict, status=200)
        else:
            result_dict = {
                'status': False,
                'message': 'Your Account is Locked please contact: kantanand.usk@gmail.com',
                'is_new_user': is_new_user,
                'username': user.username
            }
            return Response(result_dict, status=200)
    else:
        return HttpResponse('GET is not Allowed !')
        