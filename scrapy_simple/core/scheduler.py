#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
# 利用six模块实现py2和py3兼容
from six.moves.queue import Queue


class Scheduler(object):
    """
        - 缓存请求对象，为下载器提供请求对象，实现请求调度
        - 对请求对象进行去重
    """
    def __init__(self):
        self.queue = Queue()

    def add_request(self, request):
        self.queue.put(request)

    def get_request(self):
        request = self.queue.get()
        return request

    def _filter_request(self, request):
        """
        请求去重
        :param request:
        :return: bool
        """
        pass
