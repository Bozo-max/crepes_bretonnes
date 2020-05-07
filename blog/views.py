from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth import authenticate, login, logout


from datetime import datetime
from blog.models import Article
from .forms import ArticleForm, ContactForm, ConnexionForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# def home(request):
#     articles = Article.objects.all()
#
#     return render(request, 'blog/home.html.twig',locals())

class CreateUser(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'blog/user_form.html.twig'


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
    paginate_by = 5

def login_user(request):
    if request.method=='POST':
        form = ConnexionForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)

            if user:
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'blog/login_user.html.twig', locals())

def logout_user(request):
    logout(request)
    return redirect('home')

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
