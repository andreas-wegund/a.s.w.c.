from django.shortcuts import render


# Create your views here.
def listview(request):
    context = {
        'fullname': request.user.username
    }
    return render(request, 'users/home.html', context)
