from django.http import HttpResponseRedirect
from django.shortcuts import render
import subprocess
from mysite.models import Person
from django.contrib import auth
# from mysite.models import UsersOfIpv





def home(request):
    # line = Line(text="testing line one")
    # line.save()
    # user_of_ipv = UsersOfIpv(title="test", body="body")
    # user_of_ipv.save()
    context = {"val": "hello World"}
    # {'lines': Line.objects.all()}

    # print Line.objects.all()
    return render(request, "home.html", context)


def form_submit_page(request):
    first_name = request.POST['first_name']
    age = request.POST["age"]
    sex = request.POST["sex"]
    account_type = request.POST["act"]
    tags = request.POST["tag"]

    person = Person(first_name, 11, sex, account_type, tags)

    proc = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
    output = proc.stdout.read()
    lines = output.split("\n")

    context = {'lines': lines, 'person': person}

    return render(request, "form_submit_page.html", context)


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
    return render(request, 'logout.html', context={})
