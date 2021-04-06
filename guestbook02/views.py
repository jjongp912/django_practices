from django.shortcuts import render

from guestbook02.models import Guestbook


def index(request):
    results = Guestbook.objects.all().order_by('-regdate')
    data = {'guestbooklist': results}
    return render(request, 'guestbook02/index.html', data)

def add(request):

    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save()

    return HttpResponseRedirect('/guestbook02')

def deleteform(request):
    return render(request, 'guestbook02/deleteform.html')

def delete(request):
    # id = request.POST['id']
    # password = request.POST['password']
    # guestbookmodel.deleteby_no_and_password(no, password)

    guestbook = Guestbook.objects.filter(id=request.POST['id']).filter(password=request.POST['password'])
    guestbook.delete()


    return HttpResponseRedirect('/guestbook02')