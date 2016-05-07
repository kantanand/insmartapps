from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import ugettext as _

from common import constants

class LoginForm(forms.Form):
    username = forms.EmailField(required = True, widget=forms.EmailInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(required = True, widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

    def __init__(self, *args, **kwargs):
        #Variable to hold the authenticated user object
        self.user = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError(_(constants.INVALID_LOGIN))
            #user is authenticated but it is not active
            elif not self.user.is_active:
                raise forms.ValidationError(_(constants.USER_NOT_ACTIVE))
        return self.cleaned_data

    def get_user(self):
        '''
        returns the user object which got authenticated in the clean method
        '''
        return self.user