from django.conf import settings
# from django.contrib.auth.models import User
from django.db import models

from utils.abstracts.abstract_models.abstract_model import AbstractModel as AbstractModel





# Create your models here.
class Feature( AbstractModel ):
      feature_name = models.CharField( max_length=255, unique=True )
      developer = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True )
      staging_enabled = models.BooleanField( default=False )
      production_enabled = models.BooleanField( default=False )
      
      
      
      def __str__( self ):
            return self.feature_name
      
      
      class Meta( AbstractModel.Meta ):
            verbose_name = 'Feature'
            verbose_name_plural = 'Features'
