# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from .tool.bloomfulter import BloomFilter

class XxoovideoDownloaderMiddleware(object):

    def process_request(self, request, spider):
        bf = BloomFilter()

        if "html_data" in request.url:
            if bf.isContains(request.url):
                print("此链接%s已爬取，不再爬取！" % request.url)
            else:
                bf.insert(request.url)
                return None
        else:
            return None
