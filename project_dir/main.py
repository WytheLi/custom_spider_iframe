#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
from scrapy_simple.core.engine import Engine

from project_dir.spiders import DoubanSpider


if __name__ == '__main__':
    engine = Engine(DoubanSpider())
    engine.start()
