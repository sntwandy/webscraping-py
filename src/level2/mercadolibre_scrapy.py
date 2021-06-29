from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class Article(Item):
    title = Field()
    price = Field()
    description = Field()


class MercadoLibreCrawler(CrawlSpider):
    name = 'mercadoLibre'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 10
    }

    download_delay = 1

    # allowed_domains = ['https://listado.mercadolibre.com.do', 'https://articulo.mercadolibre.com.do']

    start_urls = ['https://listado.mercadolibre.com.do/celulares-smartphones']

    rules = (
        # Pagination
        Rule(
            LinkExtractor(
                allow=r'/_Desde_'
            ), follow=True
        ),
        # Detail
        Rule(
            LinkExtractor(
                allow=r'/MRD-'
            ), follow=True, callback='parse_items'
        ),
    )

    def delete_blank_space(self, text):
        new_text = text.replace('\n', '').replace('\r', '').replace('\t', '').replace('$', '').strip()
        return new_text

    def parse_items(self, response):
        try:
            item = ItemLoader(Article(), response)

            item.add_xpath('title', '//h1[@class="ui-pdp-title"]/text()', MapCompose(self.delete_blank_space))
            item.add_xpath('description', '//p[@class="ui-pdp-description__content"]/text()', MapCompose(self.delete_blank_space))
            item.add_xpath('price', '//span[@class="price-tag ui-pdp-price__part"]//span['
                                    '@class="price-tag-fraction"]/text()', MapCompose(self.delete_blank_space))
            yield item.load_item()
        except:
            print('Error')
