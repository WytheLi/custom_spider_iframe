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
        # 统计请求总数，用于判断程序退出
        self.total_request_num = 0

    def add_request(self, request):
        self.queue.put(request)
        self.total_request_num += 1

    def get_request(self):
        # request = self.queue.get()
        try:
            request = self.queue.get(False)     # 将从队列获取请求对象设置为非阻塞，否则会造成程序无法退出
        except:
            return None
        else:
            return request

    def _filter_request(self, request):
        """
        请求去重
        :param request:
        :return: bool
        """
        pass
