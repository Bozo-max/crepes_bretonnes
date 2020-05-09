from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Article(models.Model):
    titre = models.CharField(verbose_name = _("Titre de l'article"), max_length = 255)
    auteur = models.CharField(verbose_name = _("Auteur"),max_length = 255)
    content = models.TextField(verbose_name = _("Contenu"),null = True)
    date = models.DateTimeField(default = timezone.now, verbose_name = _("Date de parution"))
    categorie = models.ForeignKey('Categorie', on_delete = models.CASCADE)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = _("Article")
        ordering = ['-date']

    def __str__(self):
        return self.titre
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify("%d-%s"%(self.id, self.titre))
        super().save(*args, **kwargs)

class Categorie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):

        return self.name

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'photos/')

    def __str__(self):
        return self.nom


class Lieu(models.Model):
    adresse = models.CharField(max_length = 255)
    nom = models.CharField(max_length = 100)

    def __str__(self):
        return self.nom

class Restaurant(Lieu):
    menu = models.TextField()
