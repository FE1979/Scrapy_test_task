# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import xlwt
from web_crawl.items import VacancyItem

class ExcelExportPipeline(object):

    row = 0
    xl_file = xlwt.Workbook()
    worksheet = xl_file.add_sheet("Vacancies")


    def open_spider(self, spider):


        # add titles above
        col = 0
        for title in sorted(VacancyItem.__dict__['fields'].keys()):
            self.worksheet.write(0, col, title)
            col += 1

        # move next row for writing to file
        self.row += 1


    def close_spider(self, spider):

        self.xl_file.save(f"Vacancies_{spider.name}.xlsx")


    def process_item(self, item, spider):

        col = 0
        row = self.row

        for key in sorted(VacancyItem.__dict__['fields'].keys()):
            if key in item.keys():
                self.worksheet.write(row, col, item[key])
            col += 1

        self.row += 1

        return item
