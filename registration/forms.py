from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

class UserCreateForm(forms.Form):
    pseudo = forms.CharField(label = _("Pseudo"))
    password = forms.CharField(label = _("Mot de passe"), widget = forms.PasswordInput)
    password2 = forms.CharField(label = _("Retapez votre mot de passe"), widget = forms.PasswordInput)
    email = forms.EmailField(label = _("Votre Adresse mail"))
    is_author = forms.BooleanField(required = False, label = _("Est un auteur"))

    def clean_pseudo(self):
        username = self.cleaned_data['pseudo']

        names = User.objects.values('username')
        if {'username':username} in names:
            raise forms.ValidationError('Ce pseudo est déja utilisé')

    def clean(self):
        cleaned_data = super(UserCreateForm , self).clean()

        if cleaned_data['password'] != cleaned_data['password2']:
            self.add_error('password', 'Les mots des passe sont différents')

        return cleaned_data

class LoginForm(forms.Form):
    pseudo = forms.CharField(label = 'Votre pseudo')
    password = forms.CharField(label = 'Votre mot de passe', widget = forms.PasswordInput)
    
