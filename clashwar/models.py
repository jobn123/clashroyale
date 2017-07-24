from django.db import models
from jsonfield import JSONField

# Create your models here.
class ArenaCards(models.Model):
  title = models.CharField(max_length=30)
  percentage = models.CharField(max_length=30)
  cards = JSONField()

class PopularCards(models.Model):
  cards = JSONField()

class Decks(models.Model):
  title = models.CharField(max_length=30)
  place = models.CharField(max_length=30)
  img =  models.CharField(max_length=30)