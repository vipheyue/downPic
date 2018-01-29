import json
import re
from pprint import pprint

import scrapy
import os

from quotesbot.spiders.file_item import FileItem


# scrapy crawl DoutuZB
class DoutuZB(scrapy.Spider):
    name = "51bq"

    # start_urls = [
    #     'http://www.vipheyue.com',
    # ]

    def start_requests(self):
        yield scrapy.Request('http://img.jiefu.tv/img/attached/1/image/20160224/20160224154310_823.jpg',
                             callback=self.parse)

    def parse(self, response):
        print("----  parse  " * 40)

        image_item = FileItem()
        deal_urls = list()

        filePath = '/Volumes/Untitled/doutuCategory/zhuangbi/shengqi1.json'
        # try:
        with open(filePath, 'r') as f:
            data = json.load(f)
            myList = data['body']
            # pprint(item)
            for item in myList:
                url = "http://res.ex.51app.cn/data/"+item['emUrl']+"@G.gif"
                deal_urls.append(url)
            image_item['name'] = "i am  name"
            image_item['file_urls'] = deal_urls
            image_item['files'] = deal_urls
            yield image_item
        # except:
        #     print("小问题......")

        pass
