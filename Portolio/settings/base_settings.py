"""
Django settings for Portolio project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

### ============================================================================================ #
###  IMPORTS
### ============================================================================================ #

import os
from pathlib import Path

from dotenv import load_dotenv



### ============================================================================================ #
### GLOBAL PARAMETERS
### ============================================================================================ #
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# IF WE CREATE THE SETTINGS STRUCTURE LIKE THIS, WE NEED TO ADD ".parent" BELOW, AS THE PATH FROM
# THE SETTINGS FILE IS ONE FILE PATH DEEPER THAN THE NORMAL PATH
BASE_DIR = Path( __file__ ).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get( "DJANGO_SECRET_KEY" )

### ============================================================================================ #
### DEBUG MODE
### ============================================================================================ #
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
      case _:                 print( "======= !!!!DJANGO_RUN_MODE_ERROR!!!! ========" )

### ============================================================================================ #
### INSTALLED APPS
### ============================================================================================ #
INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      
      'django.contrib.sitemaps',  # SEO
      'django_extensions',  # Model Extensions - https://django-extensions.readthedocs.io
      
      'admin_honeypot',
      
      'users.apps.UsersConfig',  # Users APP
      'features.apps.FeaturesConfig',  # Development Features APP
]

### ============================================================================================ #
### MIDDLEWEARE
### ============================================================================================ #
MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
      'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Portolio.urls'
AUTH_USER_MODEL = 'users.CustomUser'

### ============================================================================================ #
### TEMPLATE SETTINGS
### ============================================================================================ #
# import utils.context_processors.features_enabled
TEMPLATES = [
      {
            'BACKEND':  'django.template.backends.django.DjangoTemplates',
            'DIRS':     [
                  'templates',
                  'static',
                  'staticfiles',
            ],
            'APP_DIRS': True,
            'OPTIONS':  {
                  'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                        
                        ### CUSTOM CONTEXT PROCESSOR
                        'utils.context_processors.custom_context.custom_context',
                  ],
            },
      },
]

WSGI_APPLICATION = 'Portolio.wsgi.application'

### ============================================================================================ #
### POSTGRESQL - DATABASE
### ============================================================================================ #
DATABASES = {
      'default': {
            'ENGINE': 'django.db.backends.sqlite3',  # SQLITE3
            'NAME':   BASE_DIR / 'db.sqlite3',
      },
}

### ============================================================================================ #
### PASSWORD VALIDATION
### ============================================================================================ #
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

### ============================================================================================ #
### INTERNATIONALIZATION
### ============================================================================================ #
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
