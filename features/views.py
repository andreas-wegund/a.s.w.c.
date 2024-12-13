from django.conf import settings

from .models import Feature





# Create your views here.
def feature_enabled( request, I_feature_name: str ) -> bool:
      """
            This function checks if the feature is enabled or not.
            3 OPTIONS
            - development mode & the logged-in User is the developer --> show feature
            - staging-mode is enabled and we are in staging mode
            - production mode is enabled and we are in production mode

      :param request: the request object to have the current logged-in-user
      :param I_feature_name: the name of the feature that we want to have the enabled status of
      :return: boolean indicating if the feature should be enabled (True) or not (False)
      """
      
      ENABLE_FEATURE = False
      # DEVELOPMENT
      if ((settings.DJANGO_RUN_MODE == 'DEVELOPMENT') & (Feature.objects.filter( developer__username=request.user.username, feature_name=I_feature_name ).exists())):
            ENABLE_FEATURE = True
      
      # STAGING
      elif ((settings.DJANGO_RUN_MODE == 'STAGING') & (Feature.objects.get( feature_name=I_feature_name ).staging_enabled)):
            ENABLE_FEATURE = True
      
      # PRODUCTION
      elif ((settings.DJANGO_RUN_MODE == 'PRODUCTION') & (Feature.objects.get( feature_name=I_feature_name ).production_enabled)):
            ENABLE_FEATURE = True
      
      # OTHERS
      else:
            ENABLE_FEATURE = False
      
      return ENABLE_FEATURE
