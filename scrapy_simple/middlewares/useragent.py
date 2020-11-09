#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
from scrapy_simple.conf import settings


class UserAgentMiddleware(object):
    """该中间件允许爬虫覆盖user_agent"""
    def __init__(self, user_agent="Scrapy-Simple"):
        self.user_agent = user_agent

    def from_setting_read_ua(self):
        self.user_agent = settings.USER_AGENT

    def process_request(self, request):
        """
        请求对象的预处理 -- 给请求对象headers添加User-Agent
        @param request:
        @param spider:
        @return:
        """
        self.from_setting_read_ua()
        request.headers.setdefault(b'User-Agent', self.user_agent)
