from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CreateUser

urlpatterns = [
    path('register', CreateUser.as_view(), name = 'register'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html.twig'), name = 'login'),
    path('logout', auth_views.LogoutView.as_view(template_name='registration/logout.html.twig'), name = 'logout'),
]
