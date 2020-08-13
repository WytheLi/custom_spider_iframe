#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
from scrapy_simple.core.spider import Spider


class DoubanSpider(Spider):
    start_urls = ['https://www.douban.com'] * 20

