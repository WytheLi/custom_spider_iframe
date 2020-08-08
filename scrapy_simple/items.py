#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
class Item(object):
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data
