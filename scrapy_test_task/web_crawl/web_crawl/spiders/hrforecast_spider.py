import scrapy


class JobSpider(scrapy.Spider):
    name = 'hrforecast'

    def start_requests(self):
        urls = [
            'https://www.hrforecast.de/company/career/'
            ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for job in response.css('h3 a::text').getall():
            yield {
                'Job title': job,
            }
