from .base import *
from .base import env

DEBUG = env('DJANGO_DEBUG', default=True)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SCRET_KEY', default="!!! SET SECRET_KEY !!!")

INSTALLED_APPS += [
    'django_extensions',
]
