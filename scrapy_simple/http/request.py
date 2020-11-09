#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
class Request(object):
    def __init__(self, url, method='GET', headers={}, params=None, body=None):
        """"""
        self.url = url
        self.method = method
        self.headers = headers
        self.params = params
        self.body = body
