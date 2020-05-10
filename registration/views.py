from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages

from django.views.generic import CreateView
from .forms import UserCreateForm, LoginForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate

def create_user(request):
    if request.method =='POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = User(username = cleaned_data['pseudo'],
                        email = cleaned_data['email'])

            user.set_password(cleaned_data['password'])
            if cleaned_data['is_author']:
                user.groups.add(Groups.get(name='author'))
            user.save()
            return redirect('home')
    form = UserCreateForm(request.POST or None)
    return render(request, 'registration/register.html.twig', locals())

def login_user(request):
    error = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            pseudo = form.cleaned_data['pseudo']
            password = form.cleaned_data['password']
            user = authenticate(username = pseudo, password = password)
            if user:
                login(request, user)
                messages.success(request, 'Bienvenue %s !'%(pseudo))
                return redirect(reverse('home'))
            else:
                error = True
    form = LoginForm(request.POST or None)
    return render(request, 'registration/login.html.twig', locals())

# Create your views here.
