from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('article/<int:id>', views.read_article, name = 'display_article'),
    path('article/<slug:slug>', views.read_article_by_slug, name = 'article_by_slug'),
    path('date', views.current_date, name = 'current_date'),
    path('add', views.article_form, name = 'article_form'),
    path('contact', views.contact_form, name = 'contact_form'),
]
