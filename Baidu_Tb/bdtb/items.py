# -*- coding: utf-8 -*-
import scrapy


class BdtbItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    num = scrapy.Field()
