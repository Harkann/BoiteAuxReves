from django.db import models
from django.utils import timezone

class Reve(models.Model):
    auteur = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200,blank=True)
    contenu = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    valide = models.BooleanField(default=False)
    realise = models.BooleanField(default=False)

    def __str__(self):
        return self.title+"-"+self.auteur+" : "+self.contenu[0:10]
