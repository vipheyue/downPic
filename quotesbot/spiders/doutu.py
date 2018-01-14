import json
import re

import scrapy
import os

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
        dirs = os.listdir('/Volumes/Untitled 1/tessss/')
        for file in dirs:
            print(file)
            with open('/Volumes/Untitled 1/tessss/%s'%file, 'r') as f:
                # data = json.load(f)
                data=f.readlines()
                print(data)
                # reg = r"(http\S+(png|gif|jpg$))"
                # resultList = re.findall(re.compile(reg), str(data))
                resultList = re.findall(r'/^http\S+jpg', str(data))
                print('----'*40)
                print(resultList)
                # print(resultList[0])
                print('****'*40)


    def parse(self, response):
        pass
    # def parse(self, response):
    #     os.chdir('/Volumes/Untitled1/doutu/')
    #     page = response.url.split("=")[-1]
    #     filename = '%s.json' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)