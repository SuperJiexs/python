# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from wxapp.items import WxappItem


class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=1&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.wxapp-union.com/portal.php?mod=list&catid=1&page=\d'),follow=True),
        Rule(LinkExtractor(allow=r'http://www.wxapp-union.com/article-\d{1,6}-1.html',),callback='parse_item',follow=False)

    )

    def parse_item(self, response):
        title=response.xpath('//h1[@class="ph"]/text()').get()
        authors=response.xpath('//p[@class="authors"]/a/text()').get()
        pub_time=response.xpath('//p[@class="authors"]/span/text()').get()
        content="".join(response.xpath('//td[@id="article_content"]//text()').getall()).strip()
        item=WxappItem(title=title,authors=authors,pub_time=pub_time,content=content)
        yield item