import scrapy


class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
