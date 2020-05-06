from django.urls import path
from . import views
from .models import Article
from .views import ListArticle, CreateArticle, UpdateArticle, DetailArticle

urlpatterns = [
#    path('home', views.home, name = 'home'),
    path('home', ListArticle.as_view(), name = 'home'),
    path('article/<int:id>', views.read_article, name = 'display_article'),
    path('article/<slug:slug>', DetailArticle.as_view(), name = 'article_by_slug'),
    path('date', views.current_date, name = 'current_date'),
    path('add', CreateArticle.as_view(), name = 'article_form'),
    path('update/<slug:slug>', UpdateArticle.as_view(), name = 'article_update'),
    path('contact', views.contact_form, name = 'contact_form'),
]
