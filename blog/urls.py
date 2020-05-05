from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('article/<int:id>', views.read_article, name = 'display_article'),
    path('date', views.current_date, name = 'current_date'),
    path('contact', views.contact, name = 'contact_form'),
    path('add/<int:x>/<int:y>', views.addition, name = 'add'),
]
