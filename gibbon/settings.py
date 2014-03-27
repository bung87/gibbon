# -*- coding: utf-8 -*-
"""
Django settings for server project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^$fo#ncg($2*%n$(o@vlz!^tk3*howybt3%3hrs)gq3rpjk(0i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    # 'django.contrib.sites',
    # 'threadedcomments',
    # 'django.contrib.comments',
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
)
SITE_ID = 1
# COMMENTS_APP = 'threadedcomments'
MIDDLEWARE_CLASSES = (
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.RemoteUserMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
)
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.RemoteUserBackend',
# )
# LOGIN_URL = '/login/'

ROOT_URLCONF = 'gibbon.urls'

WSGI_APPLICATION = 'gibbon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

#MEDIA_URL = '/media/'


STATIC_ROOT = os.path.join(DIRNAME, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(DIRNAME, 'static').replace('\\', '/'),
)

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    # 'django.core.context_processors.request',
    # 'django.contrib.auth.context_processors.auth',
    # 'django.core.context_processors.static',

)

if os.path.exists(os.path.join(os.path.abspath(os.path.dirname(__file__)), "local_settings.py")):
    from local_settings import *
