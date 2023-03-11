from scrapy import Request, Spider
from Algerian_Job_Market.utils import load_jobs
from Algerian_Job_Market.items import JobItem


class EmploiticComDescriptionSpider(Spider):
    name = "emploitic.com_description"
    allowed_domains = ["emploitic.com"]

    def __init__(self, load_jobs_from, **kwargs):
        super().__init__(**kwargs)
        self.jobs_list = load_jobs(load_from=load_jobs_from)

    def start_requests(self):
        for job in self.jobs_list:
            yield Request(job["link"], self.parse_job_description, cb_kwargs={"job": job})

    def parse_job_description(self, response, job):
        item = JobItem(**job)

        item.description = response.css(".details-description").get("")
        item.contract_type = response.xpath(
            '//span[contains(text(), "Type de contrat")]/following-sibling::span/text()').get()

        yield item
