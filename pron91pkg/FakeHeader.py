#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'Liangmingli'
import random
from fake_useragent import FakeUserAgent

class FakeHeader:
    """
    生成随机UserAgent
    生成随机IP
    """
    def __init__(self):
        self.ua = FakeUserAgent()
        self.language = 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4'
        self.accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'

    def prepareip(self):

        """
        生成一个随机的IP
        :return:
        """
        randIP = str(random.randint(0, 255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))

        return randIP

    def buildFakeHeader(self):
        ip = self.prepareip()
        userAgent = self.ua.random

        request_headers = {
            "Accept-Language":self.language ,
            "User-Agent":userAgent ,
            "Accept":self.accept ,
            "X-Forwarded-For":ip
        }

        return request_headers

    def buildFakeHeaderWithCookie(self,cookie):
        ip = self.prepareip()
        userAgent = self.ua.random

        request_headers = {
            "Accept-Language":self.language ,
            "User-Agent":userAgent ,
            "Accept":self.accept ,
            "X-Forwarded-For":ip,
            "cookie":cookie
        }

        return request_headers




