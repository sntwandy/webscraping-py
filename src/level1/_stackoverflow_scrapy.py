from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class Question(Item):
    id = Field()
    question = Field()
    # description = Field()

class StackOverflowSpider(Spider):
    name = 'First Spider'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    }

    start_urls = ['https://stackoverflow.com/questions']

    def _parse(self, response):
        sel = Selector(response)
        questions = sel.xpath('//div[@id="questions"]//div[@class="question-summary"]')
        i = 0
        for question in questions:
            item = ItemLoader(Question(), question)
            item.add_xpath('question', './/h3/a/text()')
            item.add_value('id', i)
            i += 1
            # item.add_xpath('description', './/div[@class="excerpt"]/text()')
            yield item.load_item()
