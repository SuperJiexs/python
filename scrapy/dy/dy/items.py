# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    dy_name = scrapy.Field()
    dy_id =scrapy.Field()
    dy_daoyan = scrapy.Field()
    dy_zhuyan = scrapy.Field()
    dy_type = scrapy.Field()
    dy_country = scrapy.Field()
    dy_yuyan = scrapy.Field()
    dy_pianchang = scrapy.Field()
    dy_riqi = scrapy.Field()
    dy_img = scrapy.Field()
    dy_desc = scrapy.Field()
    dy_xiazai = scrapy.Field()
