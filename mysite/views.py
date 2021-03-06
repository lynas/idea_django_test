from django.shortcuts import render
import subprocess
from mysite.models import Person
# from mysite.models import UsersOfIpv
from django.contrib.auth.decorators import login_required


@login_required
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



