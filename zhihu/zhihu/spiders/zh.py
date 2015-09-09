# -*- coding: utf-8 -*-
import scrapy


class ZhSpider(scrapy.Spider):
    name = "zh"
    allowed_domains = ["zhihu.com"]
    start_urls = (
        # 'http://www.zhihu.com/#signin',
        'http://www.zhihu.com/login/email',
    )

    def parse(self, response):
        # TODO: handle captcha && xsrf
        return [scrapy.FormRequest.from_response(response,
                                                formdata={"email": "xx",
                                                          "password": "xx",
                                                          "_xsrf": "xx",
                                                          "captcha": "xx",
                                                          "remember_me": "true"
                                                          },
                                                callback=self.after_login,
                                                method='POST',
                                                url='http://www.zhihu.com/login/email',
                                                )]

    def after_login(self, repsponse):
        pass
