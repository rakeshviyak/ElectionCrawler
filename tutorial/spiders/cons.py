from scrapy.contrib.spiders import CrawlSpider,Rule
# from scrapy.spider import BaseSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy import log

from tutorial.items import DmozCandidate

import json
from urlparse import urlparse


class DmozSpider(CrawlSpider):
   name = "eci_cons"
   json_data=open(r'C:\Users\rakesh viyak\Google Drive\GoogleApp\Scrappy\tutorial\states.json')
   data = json.load(json_data)
   log.start()
   s_url=[]
   a_url=[]
   for d in data:
       #s_url.append(d['link'])
       #s_url=d['link'])+","
       s_url.append(''.join([str(x) for x in d['link']]))
       a_url.append(urlparse(''.join([str(y) for y in d['link']])).hostname)
   json_data.close()
   
#    log.msg('data of start url are %s' %s_url)
    
   log.msg("Allowed Urls are %s"%a_url)
   allowed_domains=a_url
   start_urls = s_url
   print start_urls
   log.msg("The length is %s"%len(start_urls))
   log.msg('Start url are  %s' %start_urls)
   log.msg("Allowed Urls are %s"%a_url)
   rules=(
          Rule(SgmlLinkExtractor(),follow=True,callback='parse_cons'),
           
 
         # Extract links matching 'item.php' and parse them with the spider's method parse_item
         #Rule(SgmlLinkExtractor(allow=('item\.php', )), callback='parse_item'),
           )
   

   def parse_cons(self, response):
       self.log('Hi, this is an item page! %s' % response.url)
       hxs = HtmlXPathSelector(response)
       sites = hxs.select("//a[contains(@href,'.pdf')]|//a[contains(@href,'.pdf')]|//a/font/img[contains(@src,'.jpg')]|//img")
       items = []
       for site in sites:
           item = DmozCandidate()
           #item['state'] = site.select('a/font/text()').extract()
           item['candidate_link'] = site.select('@href|@src').extract()
           item['candidate_name'] = site.select('text()|@alt').extract()
           item['source_link']=response.url
           items.append(item)
       return items