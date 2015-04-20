from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect

def authenticate(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/auth/loggedin')
    else:
        return HttpResponseRedirect('/auth/invalid/')


def loggedin(request):
    context = {
        'username': request.user.username
    }
    return render(request, 'loggedin.html', context)


def login(request):
    return render(request, 'login.html', context={})


def invalid_login(request):
    return render(request, 'invalid_login.html', context={})


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html', context={})
