# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
import scrapy
import re
from scrapy.exceptions import DropItem
from os.path import join
from .merge import start 
from scrapy.utils.project import get_project_settings # scrapy 1.7后导入setting
# from scrapy.conf import setting  scrapy 1.7之前导入setting
class XxoovideoPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        header = {'Origin': 'https://baiduyunbo.com'}
        for file_url in item["file_urls"]:
            yield scrapy.Request(file_url, meta={"item": item['files']}, headers=header)

    def file_path(self, request, response=None, info=None):
        name = request.meta['item']
        videos_name = re.findall(r"\d+.ts",request.url)[0]
        return join(name, videos_name)

    def item_completed(self, results, item, info):
        file_paths = [x["path"] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no videos")
        return item
    def close_spider(self,spider):
        setting = get_project_settings()
        path = setting.get("FILES_STORE")
        start(path)
       