from scrapy import Request, Spider

class TrustmeWorkDescriptionSpider(Spider):
    name = 'trustme_work_description'
    allowed_domains = ['trustme.work']

    def __init__(self):
        self.BASE_URL = ("https://api.trustme.work/api/job_offers/%(job_hash)s"
                         "?include=technologies,job,contract_type,company")

    def start_requests(sel):
        jobs_list = []
        for job in jobs_list:
            yield Request(
                    url=self.BASE_URL % job,
                    callback=self.parse_job_description,
                    cb_kwargs={"job": job}
                    )


    def parse_job_description(self, response):
        ...

