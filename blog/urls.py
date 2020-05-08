from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from . import views
from .models import Article
from .views import ListArticle, CreateArticle, UpdateArticle, \
    DetailArticle, DeleteArticle

urlpatterns = [
#    path('home', views.home, name = 'home'),
    path('home', login_required(ListArticle.as_view()), name = 'home'),
    path('article/<int:id>', views.read_article, name = 'display_article'),
    path('article/<slug:slug>', DetailArticle.as_view(), name = 'article_by_slug'),
    path('delete/<slug:slug>', DeleteArticle.as_view(), name = 'delete_article'),
    path('date', views.current_date, name = 'current_date'),
    path('add', login_required(CreateArticle.as_view()), name = 'article_form'),
    path('update/<slug:slug>', UpdateArticle.as_view(), name = 'article_update'),
    path('contact', views.contact_form, name = 'contact_form'),
]
