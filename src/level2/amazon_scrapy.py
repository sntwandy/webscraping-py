from time import sleep

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class Product(Item):
    name = Field()
    price = Field()
    description = Field()


class Amazon(CrawlSpider):
    name = 'Hotels'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    }
    start_urls = [
        'https://www.amazon.com/s?k=macbook+pro&ref=nb_sb_noss_2']

    download_delay = 2

    rules = (
        Rule(
            LinkExtractor(
                allow=r'/dp/'
            ), follow=True, callback="parse_item"
        ),
    )

    def delete_blank_space(self, text):
        new_text = text.replace('\n', '').replace('\r', '').replace('\t', '').replace('$', '')
        return new_text

    def parse_item(self, response):
        try:
            print(response)
            sel = Selector(response)
            item = ItemLoader(Product(), sel)
            item.add_xpath('name', '//span[@id="productTitle"]/text()', MapCompose(self.delete_blank_space))
            item.add_xpath('price', '//span[@id="price_inside_buybox"]/text()', MapCompose(self.delete_blank_space))
            item.add_xpath('description', '//div[@id="productDescription"]/p/text()', MapCompose(self.delete_blank_space))

            yield item.load_item()
        except:
            print('Error')
