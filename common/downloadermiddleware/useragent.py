#coding:utf8
import random
import agent
from scrapy import log


class RandomUserAgent(object):
    '''随机UserAgent，如果settings没有设置USER_AGENT，该插件就会起作用,否则采用settings设置'''
    def __init__(self, user_agent=None):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings['USER_AGENT'])
        return o

    def process_request(self, request, spider):
        if "Scrapy" in self.user_agent:
            request.headers['User-Agent'] = random.choice(agent.AGENTS_ALL)
        else:
            request.headers.setdefault(b'User-Agent', self.user_agent)


class PCUserAgent(object):
    '''模拟手机浏览器'''
    def __init__(self, user_agent='Scrapy'):
        self.user_agent = random.choice(agent.AGENTS_PC)

    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent', self.user_agent)
        #log.msg(request.headers["User-Agent"], level=log.INFO)


class RandomPCAgent(object):
    '''模拟手机浏览器'''
    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent', random.choice(agent.AGENTS_PC))
        #log.msg(request.headers["User-Agent"], level=log.INFO)


class PhoneUserAgent(object):
    '''模拟手机浏览器'''
    def __init__(self, user_agent='Scrapy'):
        self.user_agent = random.choice(agent.AGENTS_PHONE)

    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent', self.user_agent)


class RandomPhoneAgent(object):
    '''模拟手机浏览器'''
    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent', random.choice(agent.AGENTS_PHONE))
