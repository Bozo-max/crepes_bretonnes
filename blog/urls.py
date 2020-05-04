from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('article/<int:id_article>', views.view_article),
]
