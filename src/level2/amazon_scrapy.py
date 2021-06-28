from time import sleep

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class Hotel(Item):
    name = Field()
    # price = Field()
    # description = Field()
    # amenities = Field()


class TripAdvisor(CrawlSpider):
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
            ), follow=True, callback='_parse_item'
        ),
    )

    def _parse_item(self, response):
        try:
            print(response)
            sel = Selector(response)
            item = ItemLoader(Hotel, sel)
            item.add_xpath('name', '//span[@id="productTitle"]/text()')
            # item.add_xpath('price', '//div[@class="CEf5oHnZ"]/text()')
            # item.add_xpath('description', '//div[@class="_2f_ruteS _1bona3Pu _2-hMril5"]/div[1]/text()')
            # item.add_xpath('amenities', '//div[contains(@class, "_2rdvbNSg")]/text()')

            yield item.load_item()
        except:
            print('Error')
