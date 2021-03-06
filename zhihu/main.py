__author__ = 'linliang'

from scrapy.crawler import CrawlerProcess
from zhihu.spiders.zh import ZhSpider
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
process.crawl(ZhSpider)
process.start()  # the script will block here until the crawling is finished

