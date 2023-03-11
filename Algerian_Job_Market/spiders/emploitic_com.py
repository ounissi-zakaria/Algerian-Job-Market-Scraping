from scrapy import Request, Spider
from Algerian_Job_Market.items import JobItem
from w3lib.html import remove_tags
import dateparser


class EmploiticComSpider(Spider):
    name = 'emploitic.com'
    allowed_domains = ['emploitic.com']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.DOMAIN = "https://www.emploitic.com"

    def start_requests(self):
        yield Request(f"{self.DOMAIN}/offres-d-emploi", self.parse_jobs)

    def parse_jobs(self, response):
        for listing in response.css("li.separator-bot"):
            item = JobItem()

            title_and_company = listing.css("div.bloc-right div.row-fluid")
            item.link = title_and_company.css("a::attr(href)").get("")
            item.id = item.link.split("/")[-1].split("-")[0]
            item.title = title_and_company.css("h2::text").get("").strip()
            item.company = title_and_company.css("h6 span::text").get("").strip()

            other_job_info = listing.css("div.bloc-bottom")
            item.location = remove_tags(other_job_info.css("span:has(i.fa-map-marker)").get("")).strip()
            item.published_at = dateparser.parse(remove_tags(other_job_info.css("span:has(i.fa-clock-o)").get("")))
            item.level = remove_tags(other_job_info.css("span:has(i.fa-bookmark)").get("")).strip()

            yield item

        yield self.get_next_page(response)

    def get_next_page(self, response):
        next_url = response.css('a.pagenav[title="Suivant"]::attr(href)').get()
        return response.follow(next_url, callback=self.parse_jobs)
