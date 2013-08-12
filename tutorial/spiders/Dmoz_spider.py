#from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from tutorial.items import DmozItem

class DmozSpider(CrawlSpider):
   name = "eci"
   #allowed_domains = ["http://eci.nic.in"]
   start_urls = [
       "http://eci.nic.in/eci_main/CurrentElections/ge2009/Affidavits_fs.htm"
   ]
   rules=(
          Rule(SgmlLinkExtractor(allow=('index\.htm'),tags=('frame'),attrs=('src')),callback='parse_state'),
          

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        #Rule(SgmlLinkExtractor(allow=('item\.php', )), callback='parse_item'),
          )
   

   def parse_state(self, response):
       self.log('Hi, this is an item page! %s' % response.url)
       hxs = HtmlXPathSelector(response)
       sites = hxs.select("//table/tr/td/u/b/font[text()='General Elections 2009']/../../../../../tr/td/ul/li")
       items = []
       for site in sites:
           item = DmozItem()
           item['state'] = site.select('a/font/text()').extract()
           item['link'] = site.select('a/@href').extract()
           items.append(item)
       return items