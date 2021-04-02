from django.http import HttpResponse
from django.shortcuts import render


def hello1(request):
    return HttpResponse('<h1>Hello World<h1>', content_type='text/html; charset-utf')

def hello2(request):
    return render(request, 'helloworld/hello2.html')

def tags(request):
    return render(request, 'helloworld/tags.html')