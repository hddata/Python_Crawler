# -*- coding: utf-8 -*-

import scrapy
import re
from bdtb.items import BdtbItem

class DmozSpider(scrapy.Spider):
    name = "tieba"
    allowed_domains = ["baidu.com"]
    start_urls = ["http://tieba.baidu.com/f?kw=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB&ie=utf-8"]
    #scrapy shell "http://tieba.baidu.com/f?kw=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB&ie=utf-8"
    #sel.xpath('//div[@class="t_con cleafix"]/div[@class="col2_right j_threadlist_li_right "]/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit "]/a/@title').extract()
    #sel.xpath('//div[@class="t_con cleafix"]//div[@class="col2_right j_threadlist_li_right "]/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_author pull_right"]/span/@title').extract()
    #sel.xpath('//div[@class="t_con cleafix"]/div[@class="col2_left j_threadlist_li_left"]/span[@class="threadlist_rep_num center_text"]/text()').extract()

    def parse(self, response):
        for sel in response.xpath('//div[@class="t_con cleafix"]'):
            item = BdtbItem()
            item['title'] = sel.xpath('./div[@class="col2_right j_threadlist_li_right "]/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit "]/a/@title').extract()
            item['author'] = sel.xpath('./div[@class="col2_right j_threadlist_li_right "]/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_author pull_right"]/span[@class="tb_icon_author "]/@title').re(r'(?: )(.+)')
            item['num'] = sel.xpath('./div[@class="col2_left j_threadlist_li_left"]/span[contains(@class,"threadlist_rep_num center_text")]/text()').extract()
            yield item
#scrapy crawl tieba -o info1.json -s FEED_EXPORT_ENCODING=utf-8