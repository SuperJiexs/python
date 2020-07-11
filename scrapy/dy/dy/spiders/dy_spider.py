# -*- coding: utf-8 -*-
import scrapy,time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

from dy.items import DyItem


class DySpiderSpider(CrawlSpider):
    name = 'dy_spider'
    allowed_domains = ['www.y80s.com']
    start_urls = ['http://www.y80s.com/movie/list']

    rules = (
        Rule(LinkExtractor(allow=r'movie/list/-----p(\d+)'), follow=True),
        Rule(LinkExtractor(allow=r'movie/(\d+)'), callback='parse_item', follow=False),
    )

    def __init__(self,*args,**kwargs):
        super(DySpiderSpider,self).__init__(*args,**kwargs)
        self.dy_name = "无"
        self.dy_id = "无"
        self.dy_img = "无"
        self.dy_desc = "无"
        self.dy_xiazai = "无"
        self.dy_daoyan = "无"
        self.dy_type = "无"
        self.dy_country = "无"
        self.dy_yuyan = "无"
        self.dy_pianchang = "120"
        self.dy_riqi = "2000-01-01"
        self.dy_zhuyan = "无"


    def parse_item(self, response):
        self.dy_name="".join("".join(response.xpath('//*[@id="minfo"]/div[2]/h1/text()').get()).split())
        self.dy_id = response.url.split('/')[-1]

        self.dy_img='https:'+response.xpath('//*[@id="minfo"]/div[@class="img"]/img/@src').get()

        self.dy_desc=response.xpath('//*[@id="movie_content_all"]/text()').get()
        self.dy_xiazai=response.xpath('//*[@id="myform"]/ul/li[2]/span[2]/a/@href').get()
        Dy_xx=response.xpath('//*[@id="minfo"]/div[2]/div[1]/span')
        # time.sleep(1)
        for dy_xx in Dy_xx:
            dy_xxx=(" ".join("".join(dy_xx.xpath('.//text()').getall()).split())).split('：')

            if dy_xxx[0] == '导演':
                self.dy_daoyan = " ".join(dy_xxx[1].split())

            elif dy_xxx[0] == '类型':
                self.dy_type=" ".join(dy_xxx[1].split())

            elif dy_xxx[0] == '地区':
                self.dy_country=" ".join(dy_xxx[1].split())

            elif dy_xxx[0] == '语言':
                self.dy_yuyan=" ".join(dy_xxx[1].split())

            elif dy_xxx[0] == '片长':
                self.dy_pianchang="".join(re.findall(r"\d+",(" ".join(dy_xxx[1].split()))))

            elif dy_xxx[0] == '上映日期':
                self.dy_riqi="".join(re.findall(r"\d+\-\d+\-\d+",(" ".join(dy_xxx[1].split()))))

            elif dy_xxx[0] == '演员':
                self.dy_zhuyan=" ".join(dy_xxx[1].split())


            data={
                'dy_name': self.dy_name,
                'dy_id': self.dy_id,
                'dy_daoyan':  self.dy_daoyan,
                'dy_type':  self.dy_type,
                'dy_country': self.dy_country,
                'dy_yuyan':  self.dy_yuyan,
                'dy_pianchang':self.dy_pianchang,
                'dy_riqi': self.dy_riqi,
                'dy_zhuyan': self.dy_zhuyan,
                'dy_img':self.dy_img,
                'dy_desc':self.dy_desc,
                'dy_xiazai':self.dy_xiazai,
            }

        item = DyItem(dy_name=data.get('dy_name'), dy_id=data.get('dy_id'), dy_daoyan=data.get('dy_daoyan'), dy_type=data.get('dy_type'), dy_country=data.get('dy_country'),
                      dy_yuyan=data.get('dy_yuyan'), dy_pianchang=data.get('dy_pianchang'), dy_riqi=data.get('dy_riqi'), dy_zhuyan=data.get('dy_zhuyan'),
                      dy_desc=data.get('dy_desc'), dy_img=data.get('dy_img'), dy_xiazai=data.get('dy_xiazai'))

        yield item


