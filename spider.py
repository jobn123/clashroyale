# -*- coding:utf-8 -*-
import urllib.request
import requests
from bs4 import BeautifulSoup
import ssl
import re
# import thread
import time

def tt():
  # ua  = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
  # # 初始化herder
  # headers = {
  #   'User-Agent': ua,
  # }
  # url = "http://statsroyale.com/deckbuilder/?arena=9"
  # request = urllib.request.Request(url, headers) 
  # ssl._create_default_https_context = ssl._create_unverified_context
  # response = urllib.request.urlopen(request)
  
  # html = response.read().decode('utf-8')
  # print (html)
  page = 1
  while (page <= 11):
    url = 'http://statsroyale.com/deckbuilder/?arena=' + str(page)
    r = requests.get(url)
    # get titles
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
    for t in deckbuilder:
      # popular cards
      pd = t.find_all(class_='popularDecks__decks')
      
      for p_item in pd:
        # img
        tx = p_item.find_all("img")
        print(set(tag['src'] for tag in tx))
          
        # per
        percent = p_item.find("div", class_="ui__headerBig")
        print(percent.text)

      print(len(pd))
    page = page + 1
# tt()

def getAllPopularCards():
  popularCardsurl = 'http://statsroyale.com/top/cards'
  r = requests.get(popularCardsurl)
  soup = BeautifulSoup(r.content, "html.parser")
  popularCards = soup.find_all(class_="popularCards__card")

  print(len(popularCards))
  for item in popularCards:
    im = item.find('img')
    print(im['src'])
    print(item['data-winrate'])
    print(item['data-usage'])
# getAllPopularCards()

def getAllDecks():
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
# getAllDecks()

def getArenaPopularCards():
  page = 1
  # while (page <= 11):
  arenaCardsurl = 'https://statsroyale.com/deckbuilder/?arena='+str(page)
  r = requests.get(arenaCardsurl)
  soup = BeautifulSoup(r.content, "html.parser")

  arenas = soup.find_all(class_="deckbuilder__suggestions")
  print(len(arenas))

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
      # print(set(tag['src'] for tag in img))
      # print(item.find(class_="ui__headerBig").text)
      # print(item.find_all(class_="ui__mediumText")[0].text)
      # print(item.find_all(class_="ui__mediumText")[1].text)
      
      d['imgs'] = set(tag['src'] for tag in img)
      d['winrate'] = item.find(class_="ui__headerBig").text
      d['describe'] = item.find_all(class_="ui__mediumText")[0].text
      d['subDescribe'] = item.find_all(class_="ui__mediumText")[1].text

      a.append(d)
    print(a)
getArenaPopularCards()