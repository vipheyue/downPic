# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.media import MediaPipeline
import os.path


# class QuotesbotPipeline(MediaPipeline):
class QuotesbotPipeline(FilesPipeline):
    def file_path(self,request,response=None,info=None):
        # fileName = request.meta['fileName']
        # filePath = u'full/{0}/{1}'.format("热门", fileName)
        print("+++++  "*10)
        print(request.url)
        fileName=os.path.basename(request.url)
        filePath = u'full/{0}/{1}'.format("shengqi", fileName)
        return filePath

    def get_media_requests(self, item, info):
        print("****  get_media_requests  "*20)
        # yield scrapy.Request(item['file_urls'])
        for file_url in item['file_urls']:
            yield scrapy.Request(file_url)

    def item_completed(self, results, item, info):
        # print(item)
        # print(info)
        # for x in results:
        #     print(x[0])
        #     print(x[1])
        #     print(x)
        print('--------------  '*10)

        # path = [x['path'] for ok, x in results if ok]
        # 判断图片是否下载成功，若不成功则抛出DropItem提示
        # if not path:
        #     print('--------------if not path  ')
        # print(u'正在保存图片：', item['detailURL'])
        # print(u'主题', item['title'])
        return item
