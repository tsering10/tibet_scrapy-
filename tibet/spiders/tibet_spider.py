from scrapy import Spider
from tibet.items import TibetItem


class TibetSpider(Spider):
    #name of the spider
    name = "tibet"

    # list of allowed_domains

    allowed_domains = ["tibet.net"]
    # starting url for scraping

    start_urls = [
        "https://tibet.net/category/flash-news/",
    ]

    # setting the location of the ouput csv file

    custom_settings = {
        'FEED_URI': 'tmp/tibet.csv'
    }

    def parse(self, response):
        # remove XML namespaces
        response.selector.remove_namespaces()
        # Extract article information using CSS selector

        headings = response.css("div.posts-item-title")

        for heading in headings:
            item = TibetItem()
            item['title'] = heading.css("a.posts-item-title-link h4::text").extract()[0]
            item['url'] = heading.css('div.posts-item-title a::attr(href)').extract()[0]
            yield item
