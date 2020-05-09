from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from django.utils.translation import ugettext as _
from django.utils.translation import ungettext
from django.core.paginator import Paginator, EmptyPage
from datetime import datetime
from blog.models import Article
from .forms import ArticleForm, ContactForm, ConnexionForm

# def home(request):
#     articles = Article.objects.all()
#
#     return render(request, 'blog/home.html.twig',locals())

class DeleteArticle(DeleteView):
    model = Article
    template_name = 'blog/delete_article.html.twig'
    context_object_name = 'article'
    success_url = reverse_lazy('home')

    def get_object(self, queryset = None):
        slug = self.kwargs['slug']
        return get_object_or_404(Article, slug = slug)

class DetailArticle(DetailView):
    model = Article
    template_name = 'blog/read.html.twig'

def test_i18n(request):
    nb_chats = 1
    couleur = 'blanc'
    chaine = _('Bonjour les nouveaux !')
    ip = _('Votre ip est %s') % request.META['REMOTE_ADDR']
    infos = ungettext('... et selon mes infos , vous avez %(nb)d chat %(col)s',
        '... et selon mes infos , vous avez %(nb)d chats %(col)ss', nb_chats) % {'nb':nb_chats, 'col':couleur}
    return render(request, 'blog/i18n.html.twig', locals())

class CreateArticle(SuccessMessageMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html.twig'
    success_message = "L'article a bien été créé"
    success_url = reverse_lazy('home')

class UpdateArticle(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html.twig'
    success_message = "L'article a bien été mis à jour"
    success_url = reverse_lazy('home')

    def get_object(self, queryset = None):
        slug = self.kwargs['slug']
        return get_object_or_404(Article, slug = slug)

def listArticles(request, page = 1):
    template_name = 'blog/home.html.twig'
    articles = Article.objects.order_by('-date')
    pages = Paginator(articles, 5)
    try:
        articles = pages.page(page)
    except EmptyPage:
        articles = pages.page(pages.num_pages)
    return render(request, 'blog/home.html.twig', locals())

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



def contact_form(request):
    form = ContactForm(request.POST or None, request.FILES)
    sauvegarde = False
    if form.is_valid():
        form.save()
        sauvegarde = True
    return render(request, 'blog/contact_form.html.twig', locals())
