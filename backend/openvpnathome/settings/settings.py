"""
Django settings for openvpnathome project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

ROOT_URLCONF = 'openvpnathome.urls'
WSGI_APPLICATION = 'openvpnathome.wsgi.application'

from openvpnathome.settings import USER_SETTINGS

SECRET_KEY = USER_SETTINGS.secret_key
ALLOWED_HOSTS = USER_SETTINGS.allowed_hosts
INTERNAL_IPS = USER_SETTINGS.internal_ips

from .development import *
from .installed_apps import *
from .middleware import *
from .templates import *
from .constance import *
from .restframework import *
from .auth import *
from .locale import *
from .database import *
from .static import *
from .email import *


