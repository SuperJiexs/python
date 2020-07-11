# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter
import pymysql,MySQLdb

# class DyPipeline:
#     def __init__(self):
#         self.fq = open('duanzi.json', "wb")
#         self.exporter = JsonLinesItemExporter(self.fq, ensure_ascii=False)
#
#     def open_spider(self, spider):
#         print("爬虫开始")
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spiser(self, sprder):
#         self.fq.close()
#         print("爬虫结束")

# 常规下载
# class dyPymysqlPipline(object):
#     def __init__(self):
#         mysqldata={
#             'host':'127.0.0.1',
#             'port':3306,
#             'user':'SuperJie',
#             'password':'Zxj6593955.0',
#             'database':'Flask_taopp',
#             'charset':'utf8',
#         }
#         self.conn=pymysql.connect(**mysqldata)
#         self.cursor=self.conn.cursor()
#         self._sql=None
#
#     @property
#     def sql(self):
#         if not self._sql:
#             self._sql = """
#                insert into dy(dy_name, dy_id, dy_daoyan, dy_zhuyan, by_type, dy_country, dy_yuyan, dy_pianchang, dy_riqi, dy_img, dy_desc, dy_xiazai) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
#                """
#             return self._sql
#         return self._sql
#
#
#     def process_item(self,item,spider):
#         params=(item['dy_name'],item['dy_id'],item['dy_daoyan'],item['dy_zhuyan'],item['dy_type'],item['dy_country'],item['dy_yuyan'],item['dy_pianchang'],item['dy_riqi'],item['dy_img'],item['dy_desc'],item['dy_xiazai'])
#         print(self._sql)
#         self.cursor.execute(self.sql,params)
#
#         self.conn.commit()
#
#         return item

# 异步下载
from twisted.enterprise import adbapi


class dyTwistedPiplines(object):
    def __init__(self):
        mysqldata = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'SuperJie',
            'password': 'Zxj6593955.0',
            'database': 'Flask_taopp',
            'charset': 'utf8',
            'cursorclass': pymysql.cursors.DictCursor
        }
        self.dbpool=adbapi.ConnectionPool('pymysql',**mysqldata)
        self._sql=None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                insert into dy(dy_name, dy_id, dy_daoyan, dy_zhuyan, by_type, dy_country, dy_yuyan, dy_pianchang, dy_riqi, dy_img, dy_desc, dy_xiazai,flag,is_del) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,FALSE ,FALSE );
                """
            return self._sql
        return self._sql


    def process_item(self,item,spider):
        dafer=self.dbpool.runInteraction(self.insert_item,item)
        dafer.addErrback(self.handle_error,item,spider)

    def insert_item(self,cursor,item):
        print('*'*25)
        print(item)
        print('*' * 25)
        params = (item['dy_name'], item['dy_id'], item['dy_daoyan'], item['dy_zhuyan'], item['dy_type'], item['dy_country'],item['dy_yuyan'], item['dy_pianchang'], item['dy_riqi'], item['dy_img'], item['dy_desc'], item['dy_xiazai'])
        cursor.execute(self.sql,params)

    def handle_error(self,error,item,spider):
        print(111111111111111111)
        print(error)






