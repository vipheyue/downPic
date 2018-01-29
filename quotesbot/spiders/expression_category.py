# encoding=utf-8
import scrapy
import os

from quotesbot.spiders.file_item import FileItem
from quotesbot.spiders.image_item import ImageItem


# scrapy crawl expression_category
class Expression(scrapy.Spider):
    name = "expression_category"
    start_urls = [
        'http://m.yh31.com/xq/wq/',
        # 'https://www.aitaotu.com/guonei/19181_1.html',
    ]
    def parse(self, response):
        image_item = FileItem()
        img_urls = response.xpath("//img/@src").extract()
        deal_urls = list(map(lambda x: 'm.yh31.com' + x, img_urls))  # 给图片加上域名
        deal_urls=list()
        deal_urls.append("http://m.yh31.com/tp/zjbq/201801061826485981.gif")
        print('**' * 40)
        print(deal_urls)
        image_item['file_urls'] = deal_urls
        image_item['files'] = deal_urls
        yield image_item
        print('--' * 40)
    # def parse(self, response):
    #     oldlist = response.xpath('//select[@id="Jumppage"]/option/@value').extract()
    #     deal_urls = list(map(lambda x: 'http://qq.yh31.com' + x, oldlist))  # 给所有下一页加上域名
    #     for item in deal_urls:
    #         yield scrapy.Request(item, self.downPic)
    #
    # def downPic(self, response):
    #     image_item = FileItem()
    #     img_urls = response.xpath("//img/@src").extract()
    #     deal_urls = list(map(lambda x: 'http://qq.yh31.com' + x, img_urls))  # 给图片加上域名
    #     print('**' * 40)
    #     print(deal_urls)
    #     image_item['file_urls'] = deal_urls
    #     image_item['files'] = deal_urls
    #     yield image_item
    #     print('--' * 40)
