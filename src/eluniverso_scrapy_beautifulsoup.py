from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

class News(Item):
    title = Field()
    description = Field()

class TheUniverseSpider(Spider):
    name = 'UniverseSpider'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    }
    start_urls = ['https://www.eluniverso.com/deportes/']

    def parse(self, response):
        # using scrapy
        sel = Selector(response)
        news_list = sel.xpath('//ul[@class="feed | divide-y relative  "]/li[@class="relative"]')
        for new in news_list:
            item = ItemLoader(News(), new)
            item.add_xpath('title', './/h2/a/text()')
            item.add_xpath('description', './/p/text()')

            yield item.load_item()

        # using beautiful soup
        # soup = BeautifulSoup(response.body)
        # news_container = soup.find_all('ul', class_='feed')
        #
        # for container in news_container:
        #     news = container.find_all('li', class_='relative', recursive=False)
        #     for new in news:
        #         item = ItemLoader(News(), response.body)
        #         data_container = new.find('div', class_='card')
        #         data = data_container.find('div', class_='card-content')
        #
        #         title = data.find('h2', class_='text-base').text
        #         description = data.find('p', class_='summary').text
        #
        #         item.add_value('title', title)
        #         item.add_value('description', description)
        #
        #         yield item.load_item()

