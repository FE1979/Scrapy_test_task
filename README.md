# Scrapy_test_task

Simple scrapy project parsing two sites with vacancies.

Installation:
pip install -r requirements.txt

Usage:
Run commands in the bash:
scrapy list                              - list of spiders
scrapy crawl <spider_name>               - it will export scraped data to Excel file
scrapy crawl <spider_name> -o <filename> - export in json format (with Excel too)
