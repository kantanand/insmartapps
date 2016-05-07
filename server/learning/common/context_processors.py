from django.conf import settings # import the settings file

def general_settings(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return_dict = {
        'PRODUCT_NAME': settings.PRODUCT_NAME,
        'LOGIN_URL': settings.LOGIN_URL,
        'LOGOUT_URL': settings.LOGOUT_URL,
        'LOGIN_REDIRECT_URL':settings.LOGIN_REDIRECT_URL,
    }
    return return_dict