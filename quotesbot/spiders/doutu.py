import json
import re

import scrapy
import os

from quotesbot.spiders.file_item import FileItem


class DouTu(scrapy.Spider):
    name = "doutu"

    def start_requests(self):
        urls = [
            'http://api.jiefu.tv/app2/api/dt/item/getDetail.html?itemId=6914',
            # 'http://quotes.toscrape.com/page/2/',
        ]
        # for url in urls:
        # yield scrapy.Request(url=url, callback=self.parse)

        # for index in range(1,10000):
        #     print(str(index))
        #     questurl=str('http://api.jiefu.tv/app2/api/dt/item/getDetail.html?itemId=%d'%index)
        #     yield scrapy.Request(url=questurl, callback=self.parse)
        dirs = os.listdir('/Volumes/Untitled/doutu/')
        for file in dirs:
            print(file)
            with open('/Volumes/Untitled/doutu/%s' % file, 'r') as f:
                # data = json.load(f)
                data = f.readlines()
                print(data)
                reg = r'(http\S+?(jpg|png|gif))'
                resultList = re.findall(reg, str(data))
                print('----' * 40)
                print(resultList)
                try:
                    url=resultList[0][0]
                except IndexError:
                    pass
                else:
                    yield scrapy.Request(url=url, callback=self.parse)
                # print(resultList[0])

    def parse(self, response):
        image_item = FileItem()
        deal_urls = list()
        deal_urls.append(response.url)
        print(deal_urls)
        # image_item['file_urls'] = deal_urls
        # image_item['files'] = deal_urls
        image_item['file_urls'] = deal_urls
        image_item['files'] = deal_urls
        yield image_item
        pass
        pass
    # def parse(self, response):
    #     os.chdir('/Volumes/Untitled1/doutu/')
    #     page = response.url.split("=")[-1]
    #     filename = '%s.json' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)
