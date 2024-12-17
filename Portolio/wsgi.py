"""
WSGI config for Portolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

### ============================================================================================ #
### IMPORTS
### ============================================================================================ #
import os

from django.core.wsgi import get_wsgi_application



### ============================================================================================ #
### LOGIC
### ============================================================================================ #
DJANGO_RUN_MODE = os.environ.get( "DJANGO_RUN_MODE" )
match DJANGO_RUN_MODE:
      case 'DEVELOPMENT':     os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', 'Portolio.settings.development_settings' )
      case 'STAGING':         os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', 'Portolio.settings.staging_settings' )
      case 'PRODUCTION':      os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', 'Portolio.settings.production_settings' )
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portolio.settings')

application = get_wsgi_application()
