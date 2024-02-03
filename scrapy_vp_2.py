from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Articulos(Item):
    titulo = Field()
    precio = Field()
    descripcion = Field()

class MercadoLibre(CrawlSpider):

  name = 'Mercado Libre'

  custom_settings = {
      'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
      'CLOSESPIDER_PAGECOUNT':20
      }
  
    

  allowed_domains = ['listado.mercadolibre.com.mx', 'mercadolibre.com.mx']

  start_urls = ['https://listado.mercadolibre.com.mx/laptop']

  download_delay = 1 

  rules = (
     
     Rule (

        LinkExtractor(allow=r'_Desde_'),follow=True
        
    ),      
   
     Rule(
        
        LinkExtractor(allow=r'/p/MLM'),follow=True, callback='parse_items'

     ),
     
    )
  def parse_items(self, response):
        item = ItemLoader(Articulos(),response)

        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('precio','//div[@class="ui-pdp-description pl-45 pr-45 ui-pdp-collapsable--is-collapsed"]/p/text()')
        item.add_xpath('descripcion','//div[@class= "ui-pdp-price__second-line"]/span/text()')

        yield item.load_item()

  
    

   
     



     
    
