# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join

class VacancyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    count = scrapy.Field(output_processor=TakeFirst())
    job_title = scrapy.Field(output_processor=TakeFirst())
    job_employment = scrapy.Field()
    post_date = scrapy.Field(output_processor=TakeFirst())
    region = scrapy.Field(output_processor=TakeFirst())
    employer = scrapy.Field(output_processor=TakeFirst())
    location = scrapy.Field(output_processor=TakeFirst())
    job_description = scrapy.Field(output_processor=Join())
    job_requirements = scrapy.Field(output_processor=TakeFirst())
    job_url = scrapy.Field(output_processor=TakeFirst())
    scrap_date = scrapy.Field(output_processor=TakeFirst())
