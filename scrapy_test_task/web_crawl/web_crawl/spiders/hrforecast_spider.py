import scrapy
import time
from scrapy.loader import ItemLoader
from web_crawl.items import VacancyItem


class JobSpider(scrapy.Spider):
    name = 'hrforecast'

    def start_requests(self):
        urls = [
            'https://www.hrforecast.de/company/career/'
            ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """ Collects job urls an gets data from them
        """

        jobs = []
        for job_url in response.css('h3 a::attr(href)').getall():
            jobs.append(job_url)

        for job in jobs:
            yield response.follow(job, self.parse_job)

    def parse_job(self, response):
        """ Gets job description
        """

        vacancy = ItemLoader(item=VacancyItem(), response=response)

        job_response = response.css('div.container section.av_textblock_section')[0]
        job_location = response.css('div.container section.av_textblock_section')[1]
        job_location = job_location.css('::text').get()
        job_data = job_response.css('::text').getall()
        # remove non-printable chars
        job_desc = []
        for item in job_data[5:]:
            job_desc.append(''.join(c for c in item if c.isprintable()))

        vacancy.add_value('job_title', job_data[0])
        vacancy.add_value('location', job_location)
        vacancy.add_value('job_employment', job_data[2])
        vacancy.add_value('job_description', job_desc)
        vacancy.add_value('job_url', response.url)
        vacancy.add_value('scrap_date', time.strftime('%d/%m/%Y'))

        return vacancy.load_item()
