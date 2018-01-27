# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.media import MediaPipeline


# class QuotesbotPipeline(MediaPipeline):
class QuotesbotPipeline(FilesPipeline):
    def file_path(self,request,response=None,info=None):
        print("------------- file_path")
        filename = u'full/{0}/{1}'.format("ddd", "iii")
        return filename

    def get_media_requests(self, item, info):
        print("-------------- get_media_requests  ")
        for file_url in item['file_urls']:
            yield scrapy.Request(file_url)
            # referer = item['files']
            # yield scrapy.Request(img_url, meta={'item': item, 'referer': referer})

    def item_completed(self, results, item, info):
        print('--------------item_completed  ')
        # if isinstance(item, dict) or self.files_result_field in item.fields:
        #     item[self.files_result_field] = [x for ok, x in results if ok]
        # return item
        # 创建图片存储路径
        print(item)
        print(info)
        for x in results:
            print(x[0])
            print(x[1])
            print(x)
        print('--------------  '*10)

        # path = [x['path'] for ok, x in results if ok]
        # 判断图片是否下载成功，若不成功则抛出DropItem提示
        # if not path:
        #     print('--------------if not path  ')
        # print(u'正在保存图片：', item['detailURL'])
        # print(u'主题', item['title'])
        return item
