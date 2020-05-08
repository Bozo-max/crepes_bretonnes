from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUser(CreateView):
    template_name='registration/register.html.twig'
    form_class = UserCreationForm
    model = User
    success_url = reverse_lazy('home')

# Create your views here.
