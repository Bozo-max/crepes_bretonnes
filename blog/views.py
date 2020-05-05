from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse
from datetime import datetime
from blog.models import Article

def home(request):
    articles = Article.objects.all()

    return render(request, 'blog/home.html.twig',locals())

def read_article(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/read.html.twig', {'article':article})

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
