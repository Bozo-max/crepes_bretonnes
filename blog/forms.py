from django import forms
from .models import Article

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget = forms.Textarea)
    emetteur = forms.EmailField(label = "Votre adresse mail")
    renvoi = forms.BooleanField(required = False, help_text = 'si vous cochez, ca va mal aller pour vous')

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        message = cleaned_data['message']
        sujet = cleaned_data.get('sujet')
        if 'cool' in sujet or 'cool' in message:
            raise forms.ValidationError('On est pas cool ici !')
        return cleaned_data

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['slug', 'date']
