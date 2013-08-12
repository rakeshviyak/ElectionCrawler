# from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.spider import BaseSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy import log

from tutorial.items import DmozConsti

import json
from pprint import pprint
import ast


class DmozSpider(BaseSpider):
   name = "eci_constituency"
   json_data=open(r'C:\Users\rakesh viyak\Google Drive\GoogleApp\Scrappy\tutorial\states.json')
   data = json.load(json_data)
   s_url=[]
   for d in data:
       #s_url.append(d['link'])
       #s_url=d['link'])+","
       s_url.append(''.join([str(x) for x in d['link']]))
       
   json_data.close()
   
#    log.msg('data of start url are %s' %s_url)
   allowed_domains = s_url
   
   start_urls = s_url
   log.msg('Start url are  %s' %start_urls)
#    rules=(
#           Rule(SgmlLinkExtractor(),callback='parse_continuency'),
#           
# 
#         # Extract links matching 'item.php' and parse them with the spider's method parse_item
#         #Rule(SgmlLinkExtractor(allow=('item\.php', )), callback='parse_item'),
#           )
   

   def parse(self, response):
       self.log('Hi, this is an item page! %s' % response.url)
       hxs = HtmlXPathSelector(response)
       sites = hxs.select("//a")
       items = []
       for site in sites:
           item = DmozConsti()
           #item['state'] = site.select('a/font/text()').extract()
           item['c_url'] = site.select('@href').extract()
           item['c_name']=site.select('text()').extract()
           item['state_url']=response.url
           items.append(item)
       return items