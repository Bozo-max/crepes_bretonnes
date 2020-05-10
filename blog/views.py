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
from .forms import ArticleForm
from django.contrib.auth.decorators import permission_required

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

@permission_required('blog.add_article')
def createArticle(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            a = Article(titre = cleaned_data['titre'],
                        content= cleaned_data['content'],
                        auteur = request.user,
                        categorie = cleaned_data['categorie'])
            a.save()
            messages.success(request, 'L\'article "%s" a bien été ajouté !'%cleaned_data['titre'])
            return redirect(reverse('article_by_slug', kwargs = {'slug':a.slug}))
    form = ArticleForm(request.POST or None)
    return render(request, 'blog/article_form.html.twig', locals())




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

def read_article_by_slug(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/read.html.twig', {'article':article})


def read_article(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/read.html.twig', {'article':article})
