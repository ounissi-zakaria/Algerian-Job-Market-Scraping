from scrapy import Spider, Request
from Algerian_Job_Market.items import JobItem
from datetime import datetime


class TrustmeWorkSpider(Spider):
    name = "trustme.work"

    allowed_domains = ["trustme.work"]
    start_urls = ["http://trustme.work/"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.DOMAIN = "https://trustme.work"

    def start_requests(self):
        yield Request(
            url=f"{self.DOMAIN}/_next/data/vhf0Vb-35nSvPHsW_9hYB/en.json",
            callback=self.parse_jobs,
        )

    def parse_jobs(self, response):
        data = response.json()

        jobs = data["pageProps"]["offers"]["included"]["jobs"]
        technologies = data["pageProps"]["offers"]["included"]["technologies"]
        levels = data["pageProps"]["offers"]["included"]["levels"]
        companies = data["pageProps"]["offers"]["included"]["companies"]
        contract_types = data["pageProps"]["offers"]["included"]["contract_types"]

        offers = data["pageProps"]["offers"]["data"]
        for offer in offers:
            job = JobItem()
            job.title = offer["label"]

            job.id = offer["hashid"]
            job.link = f"{self.DOMAIN}/job-offer/{job.id}"

            job.published_at = self._parse_time(offer["published_at"])
            job.created_at = self._parse_time(offer["created_at"])

            # TODO:Keep popularity somewhere
            job.technologies = [technologies[technology["id"]]["label"] for technology in offer["technologies"]]

            job.company = companies[offer["company"]["id"]]
            job.contract_type = contract_types[offer["contract_type"]["id"]]
            job.job_type = jobs[offer["job"]["id"]]
            job.level = levels[offer["level"]["id"]]
            yield job

    def _parse_time(self, date_string):
        return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
