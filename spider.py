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
tt()