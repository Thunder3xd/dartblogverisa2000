import os
from siteblog.settings import *

SECRET_KEY = 'django-insecure-i97p*5-jm3(n9vrg9wa9@zzh&hldr28bwf%wk5b)fmb*w(6^q('

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DEBUG = True

