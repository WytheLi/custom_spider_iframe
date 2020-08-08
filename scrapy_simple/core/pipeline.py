#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
class Pipeline(object):
    """
        - 负责处理数据对象，进行数据的清洗、持久化存储等等
    """

    def process_item(self, item):
        print(item)