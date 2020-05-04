from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404


def home(request):
    return HttpResponse('<h1>Hello World !</h1>')

def view_article(request, id_article):
    if id_article >100:
        raise Http404
    elif id_article == 88:
        return redirect('https://www.google.fr')
    return HttpResponse('<h1> Voici l\'article numéro %d !'%(id_article))
# Create your views here.
