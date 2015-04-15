from django.shortcuts import render
import subprocess
from mysite.models import Line
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
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    age = request.POST["age"]
    # context = {"first_name": "first_name"}

    proc = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
    output = proc.stdout.read()
    lines = output.split("\n")

    context = {'lines': lines, 'first_name': first_name}

    print(first_name, last_name, age)
    return render(request, "form_submit_page.html", context)

