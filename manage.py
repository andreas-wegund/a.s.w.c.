#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
### ============================================================================================ #
### IMPORTS
### ============================================================================================ #
import os
import sys

### ============================================================================================ #
### DOTENV
### ============================================================================================ #
from dotenv import load_dotenv



load_dotenv()





### ============================================================================================ #
### MAIN
### ============================================================================================ #
def main():
      """Run administrative tasks."""
      
      DJANGO_RUN_MODE = os.environ.get( "DJANGO_RUN_MODE" )
      match DJANGO_RUN_MODE:
            case 'DEVELOPMENT':     os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', 'Portolio.settings.development_settings' )
            case 'STAGING':         os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', 'Portolio.settings.staging_settings' )
            case 'PRODUCTION':      os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', 'Portolio.settings.production_settings' )
      
      # os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', 'Portolio.settings.development_settings' )
      try:
            from django.core.management import execute_from_command_line
      except ImportError as exc:
            raise ImportError(
                  "Couldn't import Django. Are you sure it's installed and "
                  "available on your PYTHONPATH environment variable? Did you "
                  "forget to activate a virtual environment?"
            ) from exc
      execute_from_command_line( sys.argv )





if __name__ == '__main__':
      main()
