from django.shortcuts import render
from django.conf import settings

from django.core.mail import send_mail



# Create your views here.
def listview(request):
    context = {
        'fullname': request.user.username
    }
    
    # send a mail using GMAIL
    subject = settings.ACCOUNT_EMAIL_SUBJECT_PREFIX
    message = 'Thank you for creating an account!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [ 'andreas.wegund@omv.com' ]
    send_mail( subject, message, from_email, recipient_list )

    return render(request, 'users/home.html', context)
