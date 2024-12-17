### ============================================================================================ #
###  IMPORTS
### ============================================================================================ #
### ============================================================================================ #
### DOTENV
### ============================================================================================ #

from .base_settings import *



load_dotenv()

### ============================================================================================ #
### ALLOWED_HOSTS & CSRF_TRUSTED_ORIGINS
### ============================================================================================ #
ALLOWED_HOSTS = os.environ[ "DJANGO_ALLOWED_HOSTS_" + DJANGO_RUN_MODE ].split( ' ' )
# CROSS SITE REQUEST FORGERY
CSRF_TRUSTED_ORIGINS = os.environ[ 'CSRF_TRUSTED_ORIGINS_' + DJANGO_RUN_MODE ].split( ' ' )

### ============================================================================================ #
### INTERNAL_IPS
### ============================================================================================ #
INTERNAL_IPS = [
      ##########
]

### ============================================================================================ #
### INSTALLED_APPS
### ============================================================================================ #
INSTALLED_APPS.append( 'cloudinary_storage' )
INSTALLED_APPS.append( 'django.contrib.staticfiles' )
INSTALLED_APPS.append( 'cloudinary' )

### ============================================================================================ #
### MIDDLEWARE
### ============================================================================================ #
MIDDLEWARE.append( 'whitenoise.middleware.WhiteNoiseMiddleware' )

### ============================================================================================ #
### POSTGRESQL - DATABASE
### ============================================================================================ #
import dj_database_url



DATABASES[ "prod" ] = dj_database_url.parse( os.environ.get( "DATABASE_URL" + DJANGO_RUN_MODE ) )

### ============================================================================================ #
### STATIC FILES AND MEDIA FILES & CLOUDINARY STORAGE
### ============================================================================================ #
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_STORAGE = {
      'CLOUD_NAME': os.environ.get( "CLOUDINARY_CLOUD_NAME" ),
      'API_KEY':    os.environ.get( "CLOUDINARY_API_KEY" ),
      'API_SECRET': os.environ.get( "CLOUDINARY_API_SECRET" ),
}

### ============================================================================================ #
### EMAIL SETTINGS
### ============================================================================================ #
# Create E-Mail backend from GMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get( "GMAIL_HOST_USER" )
EMAIL_HOST_PASSWORD = os.environ.get( "GMAIL_HOST_PASSWORD" )
EMAIL_USE_TLS = True  # Transport Layer Security = makes connection secure
DEFAULT_FROM_EMAIL = f'Hello from {os.environ.get( "GMAIL_HOST_USER" )}!'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'You got mail from Andreas S. Wegund!'