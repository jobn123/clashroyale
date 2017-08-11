# 爬取statsroyale网站 皇室战争相关数据

## 数据爬取
  * 爬取首页使用量最多的卡片
    * http://127.0.0.1:8000/Home
  * 爬取所有受欢迎的卡片
    * http://127.0.0.1:8000/AllPopularCards
  * 爬取所有竞技场的logo 图片
    * http://127.0.0.1:8000/AllDecks
  * 爬取所有竞技场的受欢迎的卡组
    * http://127.0.0.1:8000/clashwar

## 数据接口api
  * 获取全部竞技场受欢迎卡组
    * http://127.0.0.1:8000/api/arenaCardslists/
  * 获取全部卡片根据使用率的高低
    * http://127.0.0.1:8000/api/popularCardslists/
  * 获取全部竞技场信息
    * http://127.0.0.1:8000/api/decklists/
  * 根据竞技场id 获取 竞技场的卡组（aid = 1---11）
    * http://127.0.0.1:8000/api/getArenaCardsById/?aid=1