import scrapy


class TrustmeWorkSpider(scrapy.Spider):
    name = "trustme.work"
    allowed_domains = ["trustme.work"]
    start_urls = ["http://trustme.work/"]

    def parse(self, response):
        pass
