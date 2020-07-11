# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse

from scrapy.selector.unified import  SelectorList
from qiushi.items import QiushiItem


class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    next_urlh='https://www.qiushibaike.com'

    def parse(self, response):
        print('*' * 25)
        print(response.meta)
        print('*' * 25)
        duanzi=response.xpath('//*[@id="content"]/div/div[2]/div')
        for i in duanzi:
            dzzz=i.xpath('.//h2/text()').get().split()
            dznr="".join(i.xpath('.//div[@class="content"]/span/text()').getall()).split()
            item=QiushiItem(dzzz=dzzz,dznr=dznr)
            yield item
        next_url=response.xpath('//ul[@class="pagination"]/li/a/@href').get()

        if not next_url:
            return
        else:
            yield  scrapy.Request(self.next_urlh+next_url,callback=self.parse)



