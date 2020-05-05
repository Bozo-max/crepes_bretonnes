from django.db import models
from django.utils import timezone
from django.utils.text import slugify

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
    def save(self, *args, **kwargs):
        self.slug = slugify('%s-%s'%(str(self.date), self.titre))
        super().save(*args, **kwargs)

class Categorie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):

        return self.name
