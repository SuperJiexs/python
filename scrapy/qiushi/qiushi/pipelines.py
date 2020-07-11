# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exporters import JsonItemExporter
from scrapy.exporters import JsonLinesItemExporter

#版本一
# class QiushiPipeline:
#     def __init__(self):
#         self.fq=open('duanzi.json',"w",encoding='utf-8')
#
#     def open_spider(self,spider):
#         print("爬虫开始")
#
#     def process_item(self, item, spider):
#         item_json=json.dumps(dict(item),ensure_ascii=False)
#         self.fq.write(item_json+"\n")
#         return item
#
#
#     def close_spiser(self,sprder):
#         self.fq.close()
#         print("爬虫结束")

#版本二
# class QiushiPipeline:
#     def __init__(self):
#         self.fq = open('duanzi.json', "wb")
#         self.exporter = JsonItemExporter(self.fq, ensure_ascii=False)
#
#     def open_spider(self, spider):
#         self.exporter.start_exporting()
#         print("爬虫开始")
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spiser(self, sprder):
#         self.exporter.finish_exporting()
#         self.fq.close()
#         print("爬虫结束")


#版本三
class QiushiPipeline:
    def __init__(self):
        self.fq = open('duanzi.json', "wb")
        self.exporter = JsonLinesItemExporter(self.fq, ensure_ascii=False)

    def open_spider(self, spider):
        print("爬虫开始")


    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spiser(self, sprder):
        self.fq.close()
        print("爬虫结束")



