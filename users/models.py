from django.contrib.auth.models import AbstractUser
from django.db import models





class CustomUser( AbstractUser ):
      email = models.EmailField( max_length=100, unique=True, primary_key=True )

      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] # Required fields when createsuperuser is called



      def __str__( self ):
            return self.email
