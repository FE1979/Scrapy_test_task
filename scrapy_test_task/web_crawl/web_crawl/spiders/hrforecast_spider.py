import scrapy
import time


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
        job_response = response.css('div.container section.av_textblock_section')[0]
        job_location = response.css('div.container section.av_textblock_section')[1]
        job_location = job_location.css('::text').get()
        job_data = job_response.css('::text').getall()

        return {
            'job_title': job_data[0],
            'location': job_location,
            'job_time': job_data[2],
            'job_description': job_data[5:],
            'job_url': response.url,
            'scrap_date': time.strftime('%d/%m/%Y'),
        }
