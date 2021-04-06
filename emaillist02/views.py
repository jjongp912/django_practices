
from django.http import HttpResponse
from django.shortcuts import render
from emaillist02.models import Emaillist


def index(request):
    results = Emaillist.objects.all().order_by('-id')
    data = {"emaillist_list": results}
    return render(request, 'emaillist02/index.html', data)


def form(request):
    return render(request, 'emaillist02/form.html')


def add(request):
    emaillist = Emaillist()
    emaillist.firstname = request.POST["fn"]
    emaillist.lastname = request.POST["ln"]
    emaillist.email = request.POST["email"]

    emaillist.save()

    return HttpResponseRedirect("/emaillist02")
