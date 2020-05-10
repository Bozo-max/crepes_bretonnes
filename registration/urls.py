from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('register', views.create_user, name = 'register'),
    path('login', views.login_user, name = 'login'),
    path('logout', auth_views.LogoutView.as_view(template_name='registration/logout.html.twig'), name = 'logout'),
]
