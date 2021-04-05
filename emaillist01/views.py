
from django.shortcuts import render

from emaillist01 import models

def index(request):
    results = models.findall()
    data = { "emaillist_list": results }
    return render(request, 'emaillist01/index.html', data)

def form(request):
    return render(request, 'emaillist01/form.html')

def add(request):
    firstname = request.POST["fn"]
    lastname = request.POST["ln"]
    email = request.POST["email"]

    models.insert(firstname, lastname, email)

    return HttpResponseRedirect("/emaillist01")
    #return HttpResponse("성공했습니다.", content_type="text/html; charset-utf8")