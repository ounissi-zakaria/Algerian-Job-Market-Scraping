from scrapy import Request, Spider
from Algerian_Job_Market.items import JobItem
from Algerian_Job_Market.utils import load_jobs


class TrustmeWorkDescriptionSpider(Spider):
    name = 'trustme.work_description'
    allowed_domains = ['trustme.work']

    def __init__(self, load_jobs_from):
        self.BASE_URL = ("https://api.trustme.work/api/job_offers/%(id)s"
                         "?include=technologies,job,contract_type,company")

        self.jobs_list = load_jobs(load_from=load_jobs_from)

    def start_requests(self):
        for job in self.jobs_list:
            yield Request(url=self.BASE_URL % job, callback=self.parse_job_description, cb_kwargs={"job": job})

    def parse_job_description(self, response, job):
        item = JobItem(**job)
        item.description = response.json()["data"]["description"]
        yield item
