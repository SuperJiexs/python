# -*- coding: utf-8 -*-
import scrapy

from bmw.items import BmwItem

class BmwSpiderSpider(scrapy.Spider):
    name = 'bmw_spider'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/66.html#pvareaid=3311279']
    urlheader='https://car.autohome.com.cn/'

    def parse(self, response):
        uibox = response.xpath('//div[@class="uibox"]')[1:]
        for i in uibox:
            bmbq = i.xpath('.//div[@class="uibox-title"]/a[1]/text()').get()
            # yield  scrapy.Request(i,callback=self.img_tp)
            urlli = i.xpath('.//ul/li')[:-1]
            for j in urlli:
                urlimg = (self.urlheader + (j.xpath('.//a/@href').get()))
                yield  scrapy.Request(urlimg,callback=self.img_tp,meta={"info":{bmbq}})



    def img_tp(self,response):
        bmbq=str(response.meta.get('info'))[2:-2]
        img1=[]
        img=response.xpath('//*[@id="img"]/@src').get()
        img_new=response.urljoin(img)
        img1.append(img_new)
        print(img1)
        item=BmwItem(category=bmbq,image_urls=img1)
        yield item
        img1.pop()
