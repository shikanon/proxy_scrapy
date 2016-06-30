#coding:utf8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from collections import OrderedDict


class JsonWithEncodingPipeline(object):
    '''输出json lines文件'''
    def __init__(self):
        self.file = codecs.open('ip_proxy_utf8.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=True) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()
