from django.db import models

# Create your models here.
class Speler(models.Model):
    naam = models.CharField(max_length=25)
    voornaam = models.CharField(max_length=25)
    email = models.EmailField(max_length=50, default="no@email.be")

class Match_Punten(models.Model):
    nummerSpeler = models.IntegerField()
    punten = models.IntegerField()
    matchCode = models.IntegerField()