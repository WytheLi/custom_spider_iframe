#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
from scrapy_simple.core.spider import Spider
from scrapy_simple.items import Item


class DoubanSpider(Spider):
    # start_urls = ['https://www.douban.com'] * 20
    start_urls = ['http://movie.douban.com/top250?start=%s' % i for i in range(0, 250, 25)]     # 豆瓣电影top250列表页url

    def parse(self, response):
        """
        解析豆瓣电影top250列表页，返回标题（即电影名）
        @param response:
        @return:
        """
        for li in response.xpath("//ol[@class='grid_view']/li"):
            title = li.xpath(".//span[@class='title'][1]/text()")
            yield Item(title)
