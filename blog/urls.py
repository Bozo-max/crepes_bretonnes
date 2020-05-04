from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('article/<int:id_article>', views.view_article, name = 'display_article'),
    path('date', views.current_date, name = 'current_date'),
    path('add/<int:x>/<int:y>', views.addition, name = 'add')
]
