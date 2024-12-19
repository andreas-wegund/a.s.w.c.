### ============================================================================================ #
###  IMPORTS
### ============================================================================================ #
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
### MEDIA FILES & CLOUDINARY STORAGE
### ============================================================================================ #
# https://docs.djangoproject.com/en/5.1/howto/static-files/
MEDIA_ROOT = os.path.join( BASE_DIR, 'media' )
# STATIC_URL -> prefix for the urls in the templates where staticfiles are stored in Development
# MEDIA_URL  -> prefix like for STATIC_URL
MEDIA_URL = '/media/'
# We need to have this entry in Development as we have {% load cloudinary %} in the html templates
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

### ============================================================================================ #
### EMAIL SETTINGS
### ============================================================================================ #
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
