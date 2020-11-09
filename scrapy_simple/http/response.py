#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
import json
import re

from lxml import etree

class Response(object):
    def __init__(self, url, status_code, headers, body):
        self.url = url
        self.status_code = status_code
        self.headers = headers
        self.body = body

    def xpath(self, rule):
        """
        为响应对象封装xpath解析，用于解析响应体数据
        @param rule:
        @return:
        """
        html = etree.HTML(self.body)
        return html.xpath(rule)

    @property
    def json(self):
        """
        给响应对象封装json模块的loads方法，用于解析响应体数据
        @return:
        """
        return json.loads(self.body)

    def re_findall(self, rule, data=None):
        """
        给响应对象封装正则的findall方法，用于解析响应体数据
        @param rule:
        @param data:
        @return:
        """
        if data is None:
            data = self.body
        return re.findall(rule, data)
