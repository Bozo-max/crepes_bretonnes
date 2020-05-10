from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView
from .forms import UserCreateForm
from django.contrib.auth.models import User, Group

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

# Create your views here.
