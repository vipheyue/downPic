import scrapy


class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
# image_urls和images是固定的
