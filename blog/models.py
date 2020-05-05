from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length = 255)
    auteur = models.CharField(max_length = 255)
    content = models.TextField(null = True)
    date = models.DateTimeField(default = timezone.now, verbose_name = "Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete = models.CASCADE)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = "Article"
        ordering = ['date']

    def __str__(self):
        return self.titre

class Categorie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
