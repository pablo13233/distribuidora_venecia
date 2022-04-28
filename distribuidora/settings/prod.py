from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [www.distribuidoravenecia.com]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'distribuidora_venecia',
        'USER': 'distouno_venecia',
        'PASSWORD': '!V3n3ci4!',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

MEDIA_ROOT = BASE_DIR.parent / 'media'

MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "../static"
]




#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#MEDIA_URL = "/media/"
