# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from douban_movie.items import DoubanMovieItem


class DoubanSpider(CrawlSpider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = (
        'http://movie.douban.com/top250',
    )

    rules = (
        Rule(LinkExtractor(allow=(r"http://movie\.douban\.com/top250\?start=\d+&filter=&type=")), callback='parse_item'),
    )

    def parse_item(self, response):
        for item in response.xpath('//div[@id="content"]/div/div[1]/ol'):
            for li in item.xpath('.//li'):
                rank = li.xpath('./div/div/em/text()').extract()
                print rank

    def parse_start_url(self, response):
       self.parse_item(response)