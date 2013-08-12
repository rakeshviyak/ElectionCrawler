# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DmozItem(Item):
    state = Field()
    link = Field()

class DmozConsti(Item):
#     state=Field()
    c_url=Field()
    c_name=Field()
    state_url=Field()
    
class DmozCandidate(Item):
    candidate_link=Field()
    candidate_name=Field()
    source_link=Field()