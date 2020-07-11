# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from bmw import settings

class BmwPipeline:
    def __init__(self):
        self.odpath= os.path.join(os.path.dirname(os.path.dirname(__file__)),'imager')
        if not os.path.exists(self.odpath):
            os.mkdir(self.odpath)

    def process_item(self, item, spider):

        category=item['category']
        img_urls=item['img_urls']

        category_path= os.path.join(self.odpath,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        img_name=img_urls.split("_")[-1]
        request.urlretrieve(img_urls,os.path.join(category_path,img_name))

        return item
class BmwIMagesPipline(ImagesPipeline):
    def get_media_requests(self, item, info):

        #下载请求之前调用
        request_objs=super(BmwIMagesPipline,self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item=item
        return request_objs


    def file_path(self, request, response=None, info=None):
        #获取存放路径
        path=super(BmwIMagesPipline,self).file_path(request,response,info)
        category=request.item.get('category')
        # images_store=(settings.IMAGES_STORE).split('/')[-1]
        # print(images_store)
        # category_path=os.path.join(images_store,category)

        # if not os.path.exists(category):
            # os.mkdir(category)
        images_name=path.replace("full/","")
        image_path=os.path.join(category,images_name)
        return image_path







