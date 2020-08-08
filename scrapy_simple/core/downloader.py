#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
import requests
from scrapy_simple.http.response import Response


class Downloader(object):
    """
        - 根据请求对象，发起HTTP/HTTPS网络请求，获取响应数据，构建相应对象
    """

    def get_response(self, request):
        if request.method == 'GET':
            resp = requests.get(request.url, headers=request.headers, params=request.params)
        elif request.method == 'POST':
            resp = requests.post(request.url, data=request.body, headers=request.headers, params=request.params)
        else:
            raise Exception('不支持该请求方法！')
        return Response(resp.url, resp.status_code, resp.headers, resp.content)
