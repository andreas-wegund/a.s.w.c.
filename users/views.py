from django.shortcuts import render



app_name = 'users'





# Create your views here.
def home( request ):
      # feature_Hero = False
      # try:
      #       feature_Hero = feature_enabled( request, 'HeroButton' )
      # except:
      #       feature_Hero = False
      #
      context = {
            'fullname': request.user.username,
            # 'feature_HeroButton': feature_Hero,
      }
      #
      # # send a mail using GMAIL
      # if (settings.DJANGO_RUN_MODE == 'STAGING') | (settings.DJANGO_RUN_MODE == 'PRODUCTION'):
      #       subject = settings.ACCOUNT_EMAIL_SUBJECT_PREFIX
      #       message = 'Thank you for creating an account!'
      #       from_email = settings.DEFAULT_FROM_EMAIL
      #       recipient_list = [ 'andreas.wegund@omv.com' ]
      #       mail_result = send_mail( subject, message, from_email, recipient_list )
      #       # It will return 1 if the message was sent successfully, otherwise 0.
      
      return render( request, 'users/home.html', context )
