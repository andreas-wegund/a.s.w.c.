# Create your views here.
from django.conf import settings


### ============================================================================================ #
### CUSTOM CONTEXT PROCESSORS
### ============================================================================================ #
def custom_context( request ):
      return {
            'DJANGO_RUN_MODE': settings.DJANGO_RUN_MODE
      }
