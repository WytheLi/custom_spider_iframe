#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
from scrapy_simple.http.request import Request
from scrapy_simple.items import Item


class Spider(object):
    """
        - 构建初始请求信息，生成请求对象
        - 解析响应对象，返回数据对象或新的请求对象
    """

    start_url = ''

    def start_requests(self):
        return Request(self.start_url)

    def parse(self, response):
        """
        响应数据解析、组装为结构数据
        """
        return Item(response.body)
