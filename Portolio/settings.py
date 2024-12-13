"""
Django settings for Portolio project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

# -----------------------------------------------------------------------------#
# IMPORTS
# -----------------------------------------------------------------------------#

import os
from pathlib import Path

from dotenv import load_dotenv



# -----------------------------------------------------------------------------#
# GLOBAL PARAMETERS
# -----------------------------------------------------------------------------#
env = load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path( __file__ ).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get( "DJANGO_SECRET_KEY" )

# -----------------------------------------------------------------------------#
# SECURITY WARNING: don't run with debug turned on in production!
# -----------------------------------------------------------------------------#
DJANGO_RUN_MODES = {
      'DEVELOPMENT': True,
      'STAGING':     True,
      'PRODUCTION':  False
}
DJANGO_RUN_MODE = os.environ.get( "DJANGO_RUN_MODE" )
match DJANGO_RUN_MODE:
      case 'DEVELOPMENT':     DEBUG = DJANGO_RUN_MODES[ DJANGO_RUN_MODE ]
      case 'STAGING':         DEBUG = DJANGO_RUN_MODES[ DJANGO_RUN_MODE ]
      case 'PRODUCTION':      DEBUG = DJANGO_RUN_MODES[ DJANGO_RUN_MODE ]
      case _:                 DEBUG = False
# print( "=" * 100 )
# print( f"{os.environ.get( "DJANGO_RUN_MODE" )=} {os.environ.get( "DJANGO_RUN_MODES" )=}..... {DEBUG=}" )

ALLOWED_HOSTS = os.environ[ "DJANGO_ALLOWED_HOSTS" ].split( ' ' )

# -----------------------------------------------------------------------------#
# INSTALLED APPS
# -----------------------------------------------------------------------------#
INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      
      'django_extensions',  # Model Extensions - https://django-extensions.readthedocs.io
      
      'cloudinary_storage',
      'django.contrib.staticfiles',
      'cloudinary',
      
      'users.apps.UsersConfig',  # Users APP
      'features.apps.FeaturesConfig',  # Development Features APP
]

# -----------------------------------------------------------------------------#
# MIDDLEWEARE
# -----------------------------------------------------------------------------#
MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
      'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
      
      'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Portolio.urls'
AUTH_USER_MODEL = 'users.CustomUser'

# -----------------------------------------------------------------------------#
# TEMPLATE SETTINGS
# -----------------------------------------------------------------------------#
# import utils.context_processors.features_enabled
TEMPLATES = [
      {
            'BACKEND':  'django.template.backends.django.DjangoTemplates',
            'DIRS':     [
                  BASE_DIR / 'templates',
            ],
            'APP_DIRS': True,
            'OPTIONS':  {
                  'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                        
                        'utils.context_processors.custom_context.my_custom_context',
                  ],
            },
      },
]

WSGI_APPLICATION = 'Portolio.wsgi.application'

# -----------------------------------------------------------------------------#
# DATABASES
# -----------------------------------------------------------------------------#
import dj_database_url



DATABASES = {
      # 'default': dj_database_url.config(conn_max_age=600), # will autom. read an env var called DATABASE_URL
      
      'default': {
            'ENGINE': 'django.db.backends.sqlite3',  # SQLITE3
            'NAME':   BASE_DIR / 'db.sqlite3',
      },
      # 'development': {
      #     'ENGINE': 'django.db.backends.sqlite3',  # SQLITE3
      #     'NAME': BASE_DIR / 'db.sqlite3',
      # },
      # 'default': {
      #       'ENGINE':   'django.db.backends.postgresql',  # POSTGRESQL
      #       'NAME':     os.environ[ "POSTGRES_DB" ],  # String with the NAME of the DB
      #       'USER':     os.environ[ "POSTGRES_USER" ],
      #       'PASSWORD': os.environ[ "POSTGRES_PASSWORD" ],
      #       'HOST':     os.environ[ "POSTGRES_HOST" ],
      #       'PORT':     os.environ[ "POSTGRES_PORT" ]
      
      # },
      #     'postgresql://os.environ["POSTGRES_USER"]:os.environ["POSTGRES_PASSWORD"]@os.environ["POSTGRES_HOST"]:os.environ["POSTGRES_PORT"]/os.environ["POSTGRES_DB_NAME"]'
}
if DEBUG == False:
      DATABASES[ "prod" ] = dj_database_url.parse( os.environ.get( "DATABASE_URL" ) )

# -----------------------------------------------------------------------------#
# PASSWORD VALIDATION
# -----------------------------------------------------------------------------#
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
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

# -----------------------------------------------------------------------------#
# INTERNATIONALIZATION
# -----------------------------------------------------------------------------#
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# -----------------------------------------------------------------------------#
# STATIC FILES AND MEDIA FILES & CLOUDINARY STORAGE
# -----------------------------------------------------------------------------#
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]

MEDIA_URL = '/media/'
if DEBUG == False:
      DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
else:
      MEDIA_ROOT = BASE_DIR / 'media'

CLOUDINARY_STORAGE = {
      'CLOUD_NAME': os.environ.get( "CLOUDINARY_CLOUD_NAME" ),
      'API_KEY':    os.environ.get( "CLOUDINARY_API_KEY" ),
      'API_SECRET': os.environ.get( "CLOUDINARY_API_SECRET" ),
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------------------------------------------------------#
# EMAIL SETTINGS
# -----------------------------------------------------------------------------#
# Create E-Mail backend from GMAIL
if DJANGO_RUN_MODE == 'DEVELOPMENT':
      EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

else:
      EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
      EMAIL_HOST = 'smtp.gmail.com'
      EMAIL_PORT = 587
      EMAIL_HOST_USER = os.environ.get( "GMAIL_HOST_USER" )
      EMAIL_HOST_PASSWORD = os.environ.get( "GMAIL_HOST_PASSWORD" )
      EMAIL_USE_TLS = True  # Transport Layer Security = makes connection secure
      DEFAULT_FROM_EMAIL = f'Hello from {os.environ.get( "GMAIL_HOST_USER" )}!'
      ACCOUNT_EMAIL_SUBJECT_PREFIX = 'You got mail from Andreas S. Wegund!'
