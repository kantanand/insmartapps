"""
Django settings for learning project.

Generated by 'django-admin startproject' using Django 1.9.dev20150920101628.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zt@47tdisep-+8x4e88+(z8(r%ms!+2!#kw%s9%9l&^)2i&p^#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False#True

SESSION_COOKIE_HTTPONLY = True
SESSION_ENGINE = 'encrypted_cookies'
ALLOWED_HOSTS = [
    'localhost',
    '[SERVER_NAME]',
]
ENCRYPTED_COOKIE_KEYS = ['kmYZJ7W6yL9kdz-dA4tv_qXoAMQ_Dbl64BRh2RJFeAE=']


# Application definition
DEFAULT_APPS = (
    # Apps bundled with Django
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    # 'debug_toolbar',
)

THIRD_PARTY_APPS = (
    # Third party apps
    'ckeditor',
    'widget_tweaks',
    'django_mandrill',
    'rest_framework',
    'rest_framework_jwt',
)

LOCAL_APPS = (
    # Learning Apps
    'signup',
    'login',
    'home',
    'isaadmin',
    'datacenter',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS
EMAIL_BACKEND = 'django_mandrill.mail.backends.mandrillbackend.EmailBackend'
MANDRILL_API_KEY = "S7LYcVWRNKR70qgReZDXPw"

## Applications Settings CKEditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_RESTRICT_BY_USER = True # Setting to True will restricts access to uploaded images to the uploading user (e.g. each user only sees and uploads their own images).
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Format'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker','Undo', 'Redo'],
            ['NumberedList', 'BulletedList', 'Indent', 'Outdent', 'JustifyLeft', 'JustifyCenter','JustifyRight', 'JustifyBlock'],
            ['Image', 'Table', 'Link', 'Unlink', 'SectionLink', 'Subscript', 'Superscript'],
            ['Smiley','SpecialChar'],
        ]
    },
    'blog_toolbar':{
        'width': '765',
        'removePlugins': 'elementspath',
        'toolbar': 'BlogToolBar',
        'toolbar_BlogToolBar': [
            ['Format'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker','Undo', 'Redo'],
            ['NumberedList', 'BulletedList', 'Indent', 'Outdent', 'JustifyLeft', 'JustifyCenter','JustifyRight', 'JustifyBlock'],
            ['Image', 'Table', 'Link', 'Unlink', 'SectionLink', 'Subscript', 'Superscript'],
            ['Smiley','SpecialChar'],
        ]
    },
    'awesome_ckeditor': {
        'toolbar': 'Basic',
    },
}

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'login.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'learning.urls'

## Templates Directories ##
BASE_TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_TEMPLATE_DIR,],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'common.context_processors.general_settings',
            ],
            'loaders': [
                'app_namespace.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

WSGI_APPLICATION = 'learning.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

database_host = "[DB_HOST_NAME]"
if "DB_HOST_NAME" in database_host:
    database_host = "localhost"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "learndb",
        "USER": "admin",
        "PASSWORD": "admin@123#",
        "HOST": database_host,
        "PORT": "3306",
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_ROOT = "/home/ubuntu/static"
LOADING_STATIC_FOR_PDF = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'

MEDIA_ROOT = "/home/ubuntu/media"

# Mail Settings

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'insmartapps.in@gmail.com'
EMAIL_HOST_PASSWORD = 'insmartapps@vol'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

## GLOBAL CONSTANTS ##
host_name = "[SERVER_NAME]"
if "[SERVER_NAME]" in host_name:
    host_name = "0.0.0.0"
DEFAULT_HOST = host_name
DEFAULT_PORT = "8000"
DEFAULT_DOMAIN_NAME = DEFAULT_HOST+':'+DEFAULT_PORT
PRODUCT_NAME = 'Learning App'

AUTH_PROFILE_MODULE = 'datacenter.UserProfile'
LOGO = '/static/admin_theme/images/logo1.png'
## Login - Auth URL's ##

LOGIN_URL = '/login/'
HOME_URL = '/'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/'
LOGIN_EXEMPT_URLS = (
    # r'^$',
    r'^signup/*',
    r'^api-auth/*',
    r'^api/*',
)