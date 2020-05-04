from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from datetime import datetime


def home(request):
    return HttpResponse('<h1>Hello World !</h1><p>Vous etes sur %s </p>'%(reverse('home')))

def current_date(request):
    return render(request, 'blog/date.html.twig', {'date':datetime.now()})

def addition(request, x, y):
    res = x+y
    return render(request, 'blog/addition.html.twig', locals())

def view_article(request, id_article):
    if id_article >100:
        raise Http404
    elif id_article == 88:
        return redirect('home')
    return HttpResponse('<h1> Voici l\'article numéro %d !'%(id_article))
# Create your views here.
