from django.contrib import admin
from blog.models import Categorie, Article
from django.utils.text import Truncator


admin.site.register(Categorie)
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):

    def apercu_article(self, article):
        return Truncator(article.content).chars(40, truncate='...')

    list_display = ('titre', 'auteur', 'date', 'apercu_article')
    list_filter = ('auteur', 'categorie')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'content')
    prepopulated_fields = {'slug' : ('titre',)}

    fieldsets = (
    ('Général',{
        'classes':['collapse',],
        'fields':('titre','slug', 'auteur', 'categorie'),
    }),
    ('Contenu de l\'article',{
        'description': 'Voici une description',
        'fields':('content',)
    })
    )

admin.site.register(Article, ArticleAdmin)
