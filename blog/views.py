from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.utils.text import slugify

from datetime import datetime
from blog.models import Article
from .forms import ArticleForm, ContactForm

def home(request):
    articles = Article.objects.all()

    return render(request, 'blog/home.html.twig',locals())


def article_form(request):
    form = ArticleForm(request.POST or None)

    if form.is_valid():
        article = form.save()
        return redirect('article_by_slug',article.slug)

    return render(request, 'blog/article_form.html.twig', locals())


def read_article_by_slug(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/read.html.twig', {'article':article})


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


def contact_form(request):
    form = ContactForm(request.POST or None, request.FILES)
    sauvegarde = False
    if form.is_valid():
        form.save()
        sauvegarde = True
    return render(request, 'blog/contact_form.html.twig', locals())
