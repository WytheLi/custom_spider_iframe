#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
class SpiderMiddleware(object):
    def process_request(self, request):
        """
        请求对象的预处理
        """
        print('爬虫中间件--请求对象的预处理')
        return request

    def process_response(self, response):
        """
        响应对象的预处理
        """
        print('爬虫中间件--响应对象的预处理')
        return response
