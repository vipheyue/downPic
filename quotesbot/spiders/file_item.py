import scrapy


class FileItem(scrapy.Item):
    # name = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
# image_urls和images是固定的
