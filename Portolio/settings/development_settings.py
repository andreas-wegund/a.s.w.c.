### ============================================================================================ #
###  IMPORTS
### ============================================================================================ #
### ============================================================================================ #
### DOTENV
### ============================================================================================ #
from django.conf.global_settings import INTERNAL_IPS

from .base_settings import *



load_dotenv()

### ============================================================================================ #
### INTERNAL_IPS
### ============================================================================================ #
INTERNAL_IPS = [
      '127.0.0.1',
      'localhost',
]


### ============================================================================================ #
### ALLOWED_HOSTS & CSRF_TRUSTED_ORIGINS
### ============================================================================================ #
ALLOWED_HOSTS = os.environ[ "DJANGO_ALLOWED_HOSTS_" + DJANGO_RUN_MODE ].split( ' ' )
# CROSS SITE REQUEST FORGERY
CSRF_TRUSTED_ORIGINS = os.environ[ 'CSRF_TRUSTED_ORIGINS_' + DJANGO_RUN_MODE ].split( ' ' )

### ============================================================================================ #
### STATIC FILES AND MEDIA FILES & CLOUDINARY STORAGE
### ============================================================================================ #
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
      os.path.join( BASE_DIR, 'static' ),
      os.path.join( BASE_DIR, 'media' ),
]

STATIC_ROOT = os.path.join( BASE_DIR, 'staticfiles' )
MEDIA_ROOT = os.path.join( BASE_DIR, 'mediafiles' )

# STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'


### ============================================================================================ #
### EMAIL SETTINGS
### ============================================================================================ #
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
