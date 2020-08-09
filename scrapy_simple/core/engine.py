#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:

from .downloader import Downloader
from .scheduler import Scheduler
from .pipeline import Pipeline
from .spider import Spider
from scrapy_simple.http.request import Request
from scrapy_simple.middlewares.spider_middlewares import SpiderMiddleware
from scrapy_simple.middlewares.downloader_middlewares import DownloaderMiddleware


class Engine(object):
    """
        - 负责驱动各大组件，通过调用各组件对外提供的API接口，实现各组件间的交互与协作
        - 提供整个框架的启动入口
    """

    def __init__(self):
        self.spider = Spider()
        self.downloader = Downloader()
        self.scheduler = Scheduler()
        self.pipeline = Pipeline()

        self.spider_middleware = SpiderMiddleware()
        self.downloader_middleware = DownloaderMiddleware()

    def start(self):
        self._start_engine()

    def _start_engine(self):
        start_request = self.spider.start_requests()
        if start_request:
            start_request = self.spider_middleware.process_request(start_request)
            self.scheduler.add_request(start_request)

            request = self.scheduler.get_request()

            request = self.downloader_middleware.process_request(request)
            response = self.downloader.get_response(request)

            response = self.downloader_middleware.process_response(response)
            result = self.spider.parse(response)

            if isinstance(result, Request):
                request = self.spider_middleware.process_request(result)
                self.scheduler.add_request(request)
            else:
                item = self.spider_middleware.process_item(result)
                self.pipeline.process_item(item)
