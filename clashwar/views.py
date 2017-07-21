from django.shortcuts import render
from django.http import HttpResponse

from clashwar.models import ArenaCards
from rest_framework import generics
from .serializers import ArenaCardsSerializer

import requests
from bs4 import BeautifulSoup
import re
# Create your views here.
def Home(request):
  # return HttpResponse("Hello World!")

  getArenaCards()
  return render(request, 'index.html')
  
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


class CreateArenaCardsView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ArenaCards.objects.all()
    serializer_class = ArenaCardsSerializer
    
    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()