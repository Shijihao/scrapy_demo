# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader
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
        Rule(LinkExtractor(allow=(r"http://movie\.douban\.com/top250\?start=\d+&filter=&type=")),
             callback='parse_item'),
    )

    def parse_item(self, response):
        for item in response.xpath('//div[@id="content"]/div/div[1]/ol/li'):
            l = ItemLoader(DoubanMovieItem(), item)
            l.add_xpath('rank', './div/div/em/text()')
            l.add_xpath('picture', './div/div/a/img/@src')
            l.add_xpath('title', './div/div/div/a/span/text()')
            l.add_xpath('info', './div/div/div/p/text()')
            l.add_css('star', 'div.star em::text')
            l.add_css('quote', 'p.quote > span.inq::text')
            yield l.load_item()

    def parse_start_url(self, response):
        self.parse_item(response)
