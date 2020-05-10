from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import views as auth_views


from . import views
from .models import Article
from .views import DetailArticle, DeleteArticle

urlpatterns = [
#    path('home', views.home, name = 'home'),
    path('test_i18n', views.test_i18n, name = 'test_i18n'),
    path('home/', views.listArticles, name = 'home'),
    path('home/<int:page>', views.listArticles, name = 'home_page'),
    path('article/<int:id>', views.read_article, name = 'display_article'),
    path('article/<slug:slug>', DetailArticle.as_view(), name = 'article_by_slug'),
    path('delete/<slug:slug>', permission_required('blog.delete_article')(DeleteArticle.as_view()), name = 'delete_article'),
    path('add', views.createArticle, name = 'article_form'),
    path('update/<slug:slug>', views.updateArticle, name = 'article_update'),
]
