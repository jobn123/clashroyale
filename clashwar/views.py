from django.shortcuts import render
from django.http import HttpResponse

from clashwar.models import ArenaCards
from clashwar.models import PopularCards
from clashwar.models import Decks
from rest_framework import generics
from .serializers import ArenaCardsSerializer
from .serializers import PopularCardsSerializer
from .serializers import DecksSerializer

import requests
from bs4 import BeautifulSoup
import re
# Create your views here.
def Home(request):
  # return HttpResponse("Hello World!")

  getArenaCards()
  return render(request, 'index.html')

def AllPopularCards(request):

  getAllPopularCards()
  return HttpResponse("Hello World!")

def AllDecks(request):

  getAllDecks()
  return HttpResponse("get all decks!")

def getArenaCards():
  page = 1

  while (page <= 11):
    url = 'http://statsroyale.com/deckbuilder/?arena=' + str(page)
    r = requests.get(url)

    # get Titles
    pattern = re.compile('<div class="ui__headerSmall">(.*?)</div>', re.S)
    titles = re.findall(pattern, r.text)
    print("========第"+ str(page)+"页数据==========")
    print('============titles===============')
    print(titles)
    soup = BeautifulSoup(r.content, "html.parser")
    deckbuilder = soup.find_all(class_="deckbuilder__suggestionsGroup")
    print('============contents===============')
    print(len(deckbuilder))
    deckbuilders = []

    ac = ArenaCards()
    for t in deckbuilder:
      ac.title = "Ladder Deck Suggestions"
      # popular cards
      pd = t.find_all(class_='popularDecks__decks')
      
      for p_item in pd:
        # img
        tx = p_item.find_all("img")
        # print(set(tag['src'] for tag in tx))
        deckbuilders.append(set(tag['src'] for tag in tx))
        ac.cards = deckbuilders
        print(deckbuilders)
        # per
        percent = p_item.find("div", class_="ui__headerBig")
        ac.percentage = percent.text
        print(percent.text)
        ac.save()
      print(len(pd))
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