from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


class Noticia(Item):
    
    titular = Field()
    descripcion = Field()
    

class ElUniversoSpider (Spider):
    
    name = 'MiSegundoSpider'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }
    start_urls = ["https://www.eluniverso.com/deportes/"]
    
    def parse (self, response):
        sel = Selector(response)
        noticias = sel.xpath('//ul[@class = "feed | divide-y relative  "]/li [@class = "relative "]')
        for noticia in noticias:
           item =  ItemLoader(Noticia(), noticia)
           item.add_xpath('titular', './/h2/a/text()')
           item.add_xpath('descripcion', './/p/text()')
           
           yield item.load_item()
      