from django import forms
from .models import Article, Contact
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['slug', 'date', 'author']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class ConnexionForm(forms.Form):
    username = forms.CharField(label = "Nom d'utilisateur")
    password = forms.CharField(label = "Mot de Passe", widget = forms.PasswordInput)
