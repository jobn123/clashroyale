from django.shortcuts import render
from django.http import HttpResponse

from clashwar.models import ArenaCards
from clashwar.models import PopularCards
from clashwar.models import Decks
from clashwar.models import DeckCards

from rest_framework import generics
from rest_framework.response import Response
from .serializers import ArenaCardsSerializer
from .serializers import PopularCardsSerializer
from .serializers import DecksSerializer
from .serializers import DeckCardsSerializer

import requests
from bs4 import BeautifulSoup
import re

import json
# Create your views here.
def Home(request):
  # return HttpResponse("Hello World!")
  
  getArenaCards()
  return render(request, 'index.html')

def AllPopularCards(request):

  getAllPopularCards()
  return HttpResponse("Hello World!")

def AllDecks(request):

  # getAllDecks()
  getDeckCards()
  return HttpResponse("get all decks!")

def getArenaCards():
  page = 1
  
  while (page <= 11):
    arenaCardsurl = 'https://statsroyale.com/deckbuilder/?arena='+str(page)
    r = requests.get(arenaCardsurl)
    soup = BeautifulSoup(r.content, "html.parser")

    arenas = soup.find_all(class_="deckbuilder__suggestions")
    print(len(arenas))

    ac = ArenaCards()
    d = {'title': '', 'imgs':[], 'winrate':'', 'describe':'', 'subDescribe':''}
    a = []
    for arena in arenas:
      arenaTitle = arena.find_all(class_="ui__headerSmall")
      # for title in arenaTitle:
      # print("+++++++arenaTitle+++++++++++++" + arenaTitle[0].text)
      d['title'] =  arenaTitle[0].text
      ii = arena.find_all(class_="popularDecks__decks")
      # print(len(ii))
      
      for item in ii:
        img = item.find_all('img')

        d['imgs'] = set(tag['src'] for tag in img)
        d['winrate'] = item.find(class_="ui__headerBig").text
        d['describe'] = item.find_all(class_="ui__mediumText")[0].text
        d['subDescribe'] = item.find_all(class_="ui__mediumText")[1].text

        a.append(d)
      print(a)
      ac.cards = a
      ac.save()
    page = page + 1

# getAll popularcards
def getAllPopularCards():
  popularCardsurl = 'http://statsroyale.com/top/cards'
  r = requests.get(popularCardsurl)
  soup = BeautifulSoup(r.content, "html.parser")
  popularCards = soup.find_all(class_="popularCards__card")
  
  print(len(popularCards))
  allPopularCards = []
  pc = PopularCards()
  for item in popularCards:
    im = item.find('img')
    d = {
          "img": im['src'],
          "winrate": item['data-winrate'],
          "usage": item['data-usage']
        }
    allPopularCards.append(d)

    print(allPopularCards)
    pc.cards = allPopularCards
    pc.save()

#==================getAllDecks======================#
def getAllDecks():
  popularCardsurl = 'http://statsroyale.com'
  r = requests.get(popularCardsurl)
  soup = BeautifulSoup(r.content, "html.parser")
  decks = soup.find_all(class_="ui__card landing__arenaContainer")

  print(len(decks)) 
  for item in decks:
    dc = Decks()
    im = item.find('img')
    if im:
      dc.img = im['src']
      dc.title = item.find(class_='ui__headerSmall').text
      dc.place = item.find(class_='ui__mediumText landing__arenaValue').text
      dc.save()

def getDeckCards():
  popularCardsurl = 'http://statsroyale.com'
  r = requests.get(popularCardsurl)
  soup = BeautifulSoup(r.content, "html.parser")
  decks = soup.find_all(class_="ui__card landing__arenaContainer")
  cards = soup.find_all(class_="widget__cardMetric")
  
  cardsArr = []
  for card in cards:
    a = card.find("a")
    tt = {
      "cardImg": "https://statsroyale.com" + a['href'],
      "cardName": card.find(class_="ui__headerSmall").text,
      "cardUsage": card.find(class_="widget__cardUsageTotal").text
    }
    cardsArr.append(tt)
  decksArr = []
  for item in decks:
    im = item.find('img')
    if im:
      dd = {
        "deckImg": "https://statsroyale.com" + im['src'],
        "deckLevel": item.find(class_='ui__headerSmall').text,
        "deckPlace": item.find(class_='ui__mediumText landing__arenaValue').text
      }
      decksArr.append(dd)
  dCards = DeckCards()
  dCards.popularCards = cardsArr
  dCards.decks = decksArr
  dCards.save()

class CreateArenaCardsView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ArenaCards.objects.all()
    serializer_class = ArenaCardsSerializer
    
    def perform_create(self, serializer):
      """Save the post data when creating a new bucketlist."""
      serializer.save()

class CreatePopularCardsView(generics.ListCreateAPIView):
  """This class defines the create behavior of our rest api."""
  queryset = PopularCards.objects.all()
  serializer_class = PopularCardsSerializer

  def perform_create(self, serializer):
    """Save the post data when creating a new bucketlist."""
    serializer.save()

class CreateDecksView(generics.ListCreateAPIView):
  """This class defines the create behavior of our rest api."""
  queryset = Decks.objects.all()
  serializer_class = DecksSerializer

  def perform_create(self, serializer):
    """Save the post data when creating a new bucketlist."""
    serializer.save()

class CreateDeckCardsView(generics.ListCreateAPIView):
  """This class defines the create behavior of our rest api."""
  queryset = DeckCards.objects.all()
  serializer_class = DeckCardsSerializer

  def perform_create(self, serializer):
    """Save the post data when creating a new bucketlist."""
    serializer.save()

class ArenaCardsByIdView(generics.ListCreateAPIView):
  """This class defines the create behavior of our rest api."""
  queryset = ArenaCards.objects.all()
  serializer_class = ArenaCardsSerializer
  print('------------ArenaCardsByIdView--------------')
  # def perform_create(self, serializer):
  #   """Save the post data when creating a new bucketlist."""
  #   print(self.request.id)
  #   serializer.save()
  def list(self, list):
    id = self.request.query_params.get('aid', None)
    # id = self.aid
    print(id)
    serializer = ArenaCards.objects.get(id=id)
    response_data = {
      "success": "true",
      "msg": "success",
      "data": serializer.cards,
    }
    return Response(response_data)