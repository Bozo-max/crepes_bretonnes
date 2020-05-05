from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('article/<int:id>', views.read_article, name = 'display_article'),
    path('article/<slug:slug>', views.read_article_by_slug, name = 'article_by_slug'),
    path('date', views.current_date, name = 'current_date'),
    path('contact', views.contact, name = 'contact_form'),
    path('add/<int:x>/<int:y>', views.addition, name = 'add'),
]
