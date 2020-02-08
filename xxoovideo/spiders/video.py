# -*- coding: utf-8 -*-
import re
import time
import scrapy
from scrapy.linkextractors import LinkExtractor
from xxoovideo.items import XxoovideoItem


class VideoSpider(scrapy.Spider):
    name = 'video'
    allowed_domains = ['yj1.ceea3a8ea1f.pw']
    start_urls = ['http://yj1.ceea3a8ea1f.pw/pw/']
    # http://yj1.ceea3a8ea1f.pw/pw/html_data/111/2002/4596659.html
    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//tr[@id="fid_84"]/th/b/span/a[1]|'#[position()<2]|
                                           '//tr[@id="fid_84"]/th/span/a[1]')#[position()<2]')
        links = le.extract_links(response)
        if links:
            for link in links:
                url = link.url
                yield scrapy.Request(url, callback=self.parse_next)

    def parse_next(self, response):
        le = LinkExtractor(restrict_xpaths='//tr[position()>8]/td[2]/h3/a')
        links = le.extract_links(response)
        next_links = LinkExtractor(restrict_xpaths='//div[@id="main"]/div[10]/span[2]/div/a/')
        if links:
            for link in links:
                url = link.url
                yield scrapy.Request(url, callback=self.parse_video)
        if next:
            for next_link in next_links:
                next_url = next_link.url
                yield scrapy.Request(next_url,callback=self.parse_next)
    def parse_video(self, response):
        links_url = response.xpath('//div[@class="f14"]/iframe/@src').extract_first()
        # print(links_url)
        link_url = links_url.split("=")[1]
        # print(link_url)
        files = response.xpath("//h1/span/text()").extract_first()
        print(files)
        url = "https://m3u8.cdnpan.com/%s.m3u8" % link_url
        headers = {'Origin': 'https://baiduyunbo.com',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '\
                                 'Chrome/72.0.3626.121 Safari/537.36',
                   'Host': 'm3u8.cdnpan.com'}
        yield scrapy.Request(url,callback=self.parse_url,meta={"item":files,"link":url},headers=headers,dont_filter=True)
    def parse_url(self, response):
        print(response.url)
        # print(response.status)
        # print(response.text)
        item = XxoovideoItem()
        item['file_urls'] = re.findall(r'https://.+.com/.+.ts', response.text)
        print(item['file_urls'])

        if len(response.meta["item"]) > 20:
            item['files'] = response.meta["item"][:20]
        else:
            item['files'] = response.meta["item"]
        yield item