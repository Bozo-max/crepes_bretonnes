from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


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


class CreateArticle(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html.twig'
    success_url = reverse_lazy('home')

class UpdateArticle(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html.twig'
    success_url = reverse_lazy('home')

    def get_object(self, queryset = None):
        slug = self.kwargs['slug']
        return get_object_or_404(Article, slug = slug)

class ListArticle(ListView):
    template_name = 'blog/home.html.twig'
    model = Article
    context_object_name = 'articles'
    paginate_by = 10

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
