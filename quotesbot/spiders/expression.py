# encoding=utf-8
import scrapy
import os

from quotesbot.spiders.file_item import FileItem
from quotesbot.spiders.image_item import ImageItem


class Expression(scrapy.Spider):
    name = "expression"
    start_urls = [
        'http://qq.yh31.com/zjbq/0551964.html',
        # 'https://www.aitaotu.com/guonei/19181_1.html',
    ]

    def start_requests(self):
        with open("nextSite.txt", 'r+') as f:
            for line in f:
                dealline=str(line)[0:-1]
                print(dealline)
                yield scrapy.Request(dealline)
                pass  # do something here
            f.close()

    def parse(self, response):
        print('*****' * 40)
        image_item = FileItem()
        img_urls = response.xpath("//img/@src").extract()
        deal_urls = list(map(lambda x: 'http://qq.yh31.com' + x, img_urls))
        print(deal_urls)
        image_item['file_urls'] = deal_urls
        image_item['files'] = deal_urls
        yield image_item
        pass
        # yield scrapy.Request('http://qq.yh31.com/tp/zjbq/201712252159396323.gif', self.parse_item)

    def parse11111(self, response):
        # for item in response.xpath('//div[@id="men"]'):
        # os.mkdir("抓下来的数据")
        # os.mkdir("/Volumes/Untitled/抓下来的数据")
        # os.chdir('/Volumes/Untitled/抓下来的数据')
        for item in response.xpath('//a[@target="_self"]'):
            sub_href = item.css('a::attr(href)').extract_first()
            desc = item.css('span::text').extract_first()
            if sub_href is not None:  # 建立一个文件夹 然后开始循环
                # os.mkdir(r'%s' % desc)
                print(sub_href + "  " + desc)
                yield response.follow(sub_href, self.parse_sub)
            # yield {
            #     'href': item.css('a::attr(href)').extract_first(),
            #     'desc': item.css('span::text').extract_first()
            #
            # }

    def parse_sub(self, response):
        print("------" * 20)
        list = response.xpath('//div[@id="menu_con"]').css("a")
        for item in list:
            sub_href = item.css('a::attr(href)').extract_first()
            desc = item.css('span::text').extract_first()
            # os.mkdir(r'%s' % desc)

            # 得到子目录
            print(desc)
            print('http://qq.yh31.com' + sub_href)
            with open("site.txt", 'a+') as f:
                # f.write(str(desc))
                f.write('\n')
                f.write(str('http://qq.yh31.com' + sub_href))
            # 开始访问第一个网页
            yield response.follow(sub_href, self.parseAllNext)
        print("------" * 20)

    def parseAllNext(self, response):
        oldlist = response.xpath('//select[@id="Jumppage"]/option/@value').extract()
        print("------" * 20)
        print(oldlist)
        print("------" * 20)

        deal_urls = list(map(lambda x: 'http://qq.yh31.com' + x, oldlist))
        with open("nextSite.txt", 'a+') as f:
            for item in deal_urls:
                f.write('\n')
                f.write(str(item))
