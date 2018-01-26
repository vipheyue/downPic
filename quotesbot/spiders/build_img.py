import json
import re

import scrapy
import os

from quotesbot.spiders.file_item import FileItem


class buildimg(scrapy.Spider):
    name = "buildimg"
    start_urls = [
        'http://www.vipheyue.com',
    ]

    #
    # def start_requests(self):
    #     dirs = os.listdir('/Volumes/Untitled/doutu/')
    #     for file in dirs:
    #         with open('/Volumes/Untitled/doutu/%s' % file, 'r') as f:
    #             data = json.load(f)
    #             item = data['data']['item']
    #             url=item['picPath']
    #             word=item['name']
    #             yield scrapy.Request(url=url, callback=self.parse)
    #             pass
    # def mytest(self):
    #     print("666666666" * 40)
    #     image_item = FileItem()
    #     image_item['file_urls'] = list('http://img.jiefu.tv/img/attached/1/image/20160224/20160224154310_823.jpg')
    #     image_item['files'] = list('http://img.jiefu.tv/img/attached/1/image/20160224/20160224154310_823.jpg')
    #     yield image_item
        # with open('/Volumes/Untitled/doutu/8.json', 'r') as f:
        #     data = json.load(f)
        #     item = data['data']['item']
        #     url = item['picPath']
        #     word = item['name']
        #     print(word)
        #     # 开始下载
        #     image_item = FileItem()
        #     image_item['file_urls'] = list(url)
        #     image_item['files'] = list(url)
        #     yield image_item
        #     pass

    def parse(self, response):
        print("----" * 40)
        # self.mytest()
        # print(str(response.url))

        # yield scrapy.Request(url='http://img.jiefu.tv/img/attached/1/image/20160224/20160224154310_823.jpg',callback=self.parse22)

        image_item = FileItem()
        deal_urls = list()
        deal_urls.append('http://img.jiefu.tv/img/attached/1/image/20160224/20160224154310_823.jpg')
        # image_item['name'] = "i am  name"
        image_item['file_urls'] = deal_urls
        image_item['files'] = deal_urls
        yield image_item
        pass
