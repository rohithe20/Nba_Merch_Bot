# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 15:48:08 2022

@author: rohit
"""

import scrapy
from scrapy.crawler import CrawlerProcess
import json
from prettytable import PrettyTable


from navigating.navigating import Navigating  
from selenium.webdriver.support.ui import WebDriverWait


class Nba_Crawler(scrapy.Spider) :
   name = "jersey_scraper"
   teamname = str(input("Choose your team. Formate eg: Memphis Grizzlies :"))
   login_attempt_correct = False
   user_attempt_correct = False
   team_list = ["Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls",
                "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets", "Detroit Pistons", "Golden State Warriors",
                "Houston Rockets", "Indiana Pacers", "Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies",
                "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks",
                "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns",
                "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", "Utah Jazz",
                "Washington Wizards"]

   user_category_list = ["Men", "Women", "Kids"]
   while not login_attempt_correct:
        if teamname.strip() in team_list:
         login_attempt_correct = True
        else:
          teamname = str(input("You have not entered the team in the correct format. Format eg, Boston Celtics:"))

   usercategory = str(input("Choose a category from Men, Women, and Kids :"))
   while not user_attempt_correct :
       if usercategory.strip() in user_category_list :
          user_attempt_correct = True
       else:
          usercategory = str(input("Please enter category exactly as listed above:"))

   inst = Navigating()
   inst.landing_page()
   inst.choose_team(teamname.strip())
   inst.choose_category(usercategory.strip())
   inst.select_jersey()
   sourceUrl = str(inst.current_url)
   start_urls = [sourceUrl]

  
   def parse(self, response):
      collection = []
      for jersey_section in response.css("div.product-card") :
              jersey_name = jersey_section.css('div.columns div.card-image-container div.product-image-container a img::attr(alt)').get()
              jersey_price = jersey_section.css('div.price-row span.money-value span.sr-only::text').get()
              collection.append([jersey_name, jersey_price])
      next_page = response.xpath('//li[@class = "next-page"]')
      if next_page:
        url = response.urljoin(next_page[0].extract())
        yield scrapy.Request(url, self.parse)
      table = PrettyTable(field_names = ["Top_Selling_Jersey", "Price"])
      table.align["Top_Selling_Jersey"] = "l"
      table.add_rows(collection)
      print(table)


process = CrawlerProcess()
process.crawl(Nba_Crawler)
process.start()
      


 
  
