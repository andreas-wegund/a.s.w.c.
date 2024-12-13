from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from features.views import feature_enabled





# Create your views here.
def listview( request ):
      feature_Hero = False
      try:
            feature_Hero = feature_enabled( request, 'HeroButton' )
      except:
            feature_Hero = False
      
      context = {
            'fullname':           request.user.username,
            'feature_HeroButton': feature_Hero,
      }
      
      # send a mail using GMAIL
      if (settings.DJANGO_RUN_MODE == 'STAGING') | (settings.DJANGO_RUN_MODE == 'PRODUCTION'):
            subject = settings.ACCOUNT_EMAIL_SUBJECT_PREFIX
            message = 'Thank you for creating an account!'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [ 'andreas.wegund@omv.com' ]
            send_mail( subject, message, from_email, recipient_list )
      
      return render( request, 'users/home.html', context )
