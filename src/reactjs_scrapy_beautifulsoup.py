from scrapy.item import Field
from scrapy.item import Item
from scrapy.selector import Selector
from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess


class ReactJSDoc(Item):
    title = Field()


class ReactJSDocumentation(Spider):
    name = 'ReactJSSpider'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    }
    start_urls = ['https://reactjs.org/docs/getting-started.html']

    def parse(self, response):
        sel = Selector(response)
        doc_list_titles = sel.xpath('//div[@class="css-15weewl"]//h3')

        for doc in doc_list_titles:
            item = ItemLoader(ReactJSDoc(), doc)
            item.add_xpath('title', './text()')

            yield item.load_item()


# process = CrawlerProcess({
#     'FEED_URI': 'data.csv',
#     'FEED_FORMAT': 'csv',
# })
#
# process.crawl(ReactJSDocumentation)
# process.start()
