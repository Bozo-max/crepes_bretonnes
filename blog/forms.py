from django import forms
from .models import Article, Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['slug', 'date']
