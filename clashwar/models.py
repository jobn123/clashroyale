from django.db import models
from jsonfield import JSONField

# Create your models here.
class ArenaCards(models.Model):
  cards = JSONField()

class PopularCards(models.Model):
  cards = JSONField()

class Decks(models.Model):
  title = models.CharField(max_length=30)
  place = models.CharField(max_length=100)
  img =  models.CharField(max_length=30)

class DeckCards(models.Model):
  popularCards = JSONField()
  decks = JSONField()

class PopularDecks(models.Model):
  winrate = models.CharField(max_length=30)
  imgs = JSONField()