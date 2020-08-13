#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
import datetime
import time

from .downloader import Downloader
from .scheduler import Scheduler
from .pipeline import Pipeline
# from .spider import Spider
from scrapy_simple.http.request import Request
from scrapy_simple.middlewares.spider_middlewares import SpiderMiddleware
from scrapy_simple.middlewares.downloader_middlewares import DownloaderMiddleware
from scrapy_simple.utils.log import logger


class Engine(object):
    """
        - 负责驱动各大组件，通过调用各组件对外提供的API接口，实现各组件间的交互与协作
        - 提供整个框架的启动入口
    """

    def __init__(self, spider):
        # self.spider = Spider()
        self.spider = spider
        self.downloader = Downloader()
        self.scheduler = Scheduler()
        self.pipeline = Pipeline()

        self.spider_middleware = SpiderMiddleware()
        self.downloader_middleware = DownloaderMiddleware()

        self.total_request_nums = 0
        self.total_response_nums = 0

    def start(self):
        start_time = datetime.datetime.now()
        logger.info('项目启动时间： %s' % start_time)
        self._start_engine()
        end_time = datetime.datetime.now()
        logger.info('项目终止时间： %s' % end_time)
        logger.info('项目耗时： %.2f' % (end_time - start_time).total_seconds())

        logger.info('总的请求数量： %s' % self.total_request_nums)
        logger.info('总的响应数量： %s' % self.total_response_nums)

    def _start_engine(self):
        # start_request = self.spider.start_requests()
        # if start_request:
        #     start_request = self.spider_middleware.process_request(start_request)
        #     self.scheduler.add_request(start_request)
        #
        #     request = self.scheduler.get_request()
        #
        #     request = self.downloader_middleware.process_request(request)
        #     response = self.downloader.get_response(request)
        #
        #     response = self.downloader_middleware.process_response(response)
        #     response = self.spider_middleware.process_response(response)
        #     result = self.spider.parse(response)
        #
        #     if isinstance(result, Request):
        #         request = self.spider_middleware.process_request(result)
        #         self.scheduler.add_request(request)
        #     else:
        #         self.pipeline.process_item(item)
        self._add_request()
        while True:
            time.sleep(0.001)
            # 循环取出队列中的请求对象，下载解析数据
            self._execute_download_parse()
            if self.total_response_nums >= self.total_request_nums:
                break

    def _add_request(self):
        for start_request in self.spider.start_requests():
            start_request = self.spider_middleware.process_request(start_request)

            self.scheduler.add_request(start_request)
            self.total_request_nums += 1

    def _execute_download_parse(self):
        request = self.scheduler.get_request()
        if not request:
            return
        request = self.downloader_middleware.process_request(request)
        response = self.downloader.get_response(request)
        response = self.downloader_middleware.process_response(response)

        response = self.spider_middleware.process_response(response)

        # 遍历生成器（yield返回的解析结果）
        for result in self.spider.parse(response):
            if isinstance(result, Request):
                request = self.spider_middleware.process_request(result)
                self.scheduler.add_request(request)
                self.total_request_nums += 1
            else:
                self.pipeline.process_item(result)
        self.total_response_nums += 1

