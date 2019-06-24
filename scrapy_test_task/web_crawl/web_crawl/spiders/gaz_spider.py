import scrapy
import time


class GazpromSpider(scrapy.Spider):

    name = 'gaz_spider'

    base_url = 'https://www.gazpromvacancy.ru/'
    start_url = base_url + 'vacancies/'
    count = 0


    def start_requests(self):

        yield scrapy.Request(self.start_url, callback=self.parse)

    def parse(self, response):
        """ Moves through pages and scrap every vacancy
        """

        # get vacancy count
        jobs_found = response.css('span.jobs-found strong::text').get()

        # get vacancies urls on the current page
        jobs_list = response.css('div.list-container').css('div.item')
        job_urls = [job.css('a::attr(href)').get() for job in jobs_list]

        for url in job_urls:
            yield response.follow(self.base_url+url, self.parse_job)

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            next_page = self.base_url + next_page
            yield scrapy.Request(next_page, callback=self.parse)



    def parse_job(self, response):
        """ Gets job description
        """

        self.count += 1

        job_desc = ''.join(item for item in \
            response.css('div.job-description').css('::text').getall())
        job_desc = ''.join(c for c in job_desc if c.isprintable())

        job_reqs = ''.join(item for item in \
            response.css('div.job-requirements').css('::text').getall())
        job_reqs = ''.join(c for c in job_reqs if c.isprintable())

        yield {
            'count': self.count,
            'job_title': response.css('h1.mainHeader::text').get() ,
            'post_date': ''.join(c for c in \
                                 response.css('span.date::text').get() if \
                                 c.isprintable()),
            'region': ''.join(c for c in \
                                 response.css('span.region::text').get() if \
                                 c.isprintable()),
            'employer': response.css('div.employer dd::text').get(),
            'location': response.css('div.location dd::text').get(),
            'job_description': job_desc,
            'job_requirements': job_reqs,
            'scrap_date': time.strftime('%d/%m/%Y'),
        }
