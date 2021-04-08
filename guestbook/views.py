from django.shortcuts import render
from guestbook.models import Guestbook


def index(request):
    results = Guestbook.objects.all().order_by('-regdate')
    data = {'guestbooklist': results}
    return render(request, 'guestbook/index.html', data)

def deleteform(request):
    return render(request, 'guestbook/deleteform.html')

def add(request):

    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')