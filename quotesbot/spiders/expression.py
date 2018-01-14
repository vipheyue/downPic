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
    # def parse(self, response):
    #     for quote in response.css('div.quote'):
    #         yield {
    #             'text': quote.css('span.text::text').extract_first(),
    #             'author': quote.xpath('span/small/text()').extract_first(),
    #         }
    #
    #     next_page = response.css('li.next a::attr("href")').extract_first()
    #     if next_page is not None:
    #         yield response.follow(next_page, self.parse)

    def __parse_pic(self, response):
        image_item = ImageItem()
        # img_urls = response.xpath("//img/@src").extract()
        img_urls = ['http://qq.yh31.com/tp/zjbq/201712252159396323.gif']
        print(img_urls)
        # for item in img_urls:
        #     yield scrapy.Request(item, self.parse_item)

        image_item['image_urls'] = img_urls
        image_item['images'] = img_urls

        yield image_item

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

        # for item in response.xpath('//div[@id="menu_con"]'):
        #         sub_href = subItem.css('a::attr(href)').extract_first()
        #         yield {
        #             'name222222':item
        #         }

    # def getCurrentAllSite(self,response):
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

    def browseSite(self, response):
        # 下载图片
        # self.downPic(response)
        # print('******' * 40)
        # image_item = FileItem()
        # # img_urls = ['http://qq.yh31.com/tp/zjbq/201712252159396323.gif']
        # # image_item['file_urls'] = img_urls
        # img_urls = response.xpath("//img/@src").extract()
        # deal_urls = list(map(lambda x: 'http://qq.yh31.com' + x, img_urls))
        # print(deal_urls)
        # image_item['file_urls'] = deal_urls
        # image_item['files'] = deal_urls
        # yield image_item

        # 解析第二页
        list = response.xpath('//div[@class="c_bot_fy"]').css("a")
        # 取最后一个 遍历下一页
        print("00" * 30)
        print(len(list))
        if len(list) > 1:
            lastItem = list[len(list) - 1]
            desc = lastItem.css('a::text').extract_first()
            next_href = lastItem.css('a::attr(href)').extract_first()
            print(desc + "  " + next_href)

            with open("dealSite.txt", 'a+') as f:
                # f.write(str(desc))
                f.write('\n')
                f.write(str('http://qq.yh31.com' + next_href))
            # 开始访问第一个网页

            yield response.follow(next_href, self.browseSite)

    def downPic(self, response):
        print('*****' * 40)
        image_item = FileItem()
        # img_urls = ['http://qq.yh31.com/tp/zjbq/201712252159396323.gif']
        # image_item['file_urls'] = img_urls
        img_urls = response.xpath("//img/@src").extract()
        deal_urls = list(map(lambda x: 'http://qq.yh31.com' + x, img_urls))
        print(deal_urls)
        image_item['file_urls'] = deal_urls
        image_item['files'] = deal_urls
        yield image_item

    def parse_item(self, response):
        with open("site.txt", 'r+') as f:
            for line in f:
                print(str(line))
                yield response.follow(line, self.downPic)
                pass  # do something here
            f.close()

            pass
