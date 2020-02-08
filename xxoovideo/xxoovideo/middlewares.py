# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from .tool.bloomfulter import BloomFilter

class XxoovideoDownloaderMiddleware(object):
    def __init__(self):

        self.bf = BloomFilter()

    def process_request(self, request, spider):

        if "html_data" in request.url:
            if self.bf.isContains(request.url):
                print("此链接%s已爬取，不再爬取！" % request.url)
        else:
            return None

    def process_response(self,request,response,spider):
        if response.status == 200 and "html_data" in response.url:
            self.bf.insert(response.url)
        return response