import scrapy


class EmploiticComSpider(scrapy.Spider):
    name = 'emploitic.com'
    allowed_domains = ['emploitic.com']
    start_urls = ['http://emploitic.com/']

    def parse(self, response):
        pass
