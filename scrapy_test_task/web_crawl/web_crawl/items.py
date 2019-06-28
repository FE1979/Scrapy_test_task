# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VacancyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    count = scrapy.Field()
    job_title = scrapy.Field()
    post_date = scrapy.Field()
    region = scrapy.Field()
    employer = scrapy.Field()
    location = scrapy.Field()
    job_description = scrapy.Field()
    job_requirements = scrapy.Field()
    job_url = scrapy.Field()
    scrap_date = scrapy.Field()
