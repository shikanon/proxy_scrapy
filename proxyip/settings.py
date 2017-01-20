# -*- coding: utf-8 -*-
# author: shikanon
# Scrapy settings for proxyip project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'proxyip'

SPIDER_MODULES = ['proxyip.spiders']
NEWSPIDER_MODULE = 'proxyip.spiders'
#是否启动cookies
COOKIES_ENABLED = False
#log级别CRITICAL、 ERROR、WARNING、INFO、DEBUG
LOG_LEVEL = "DEBUG"
#是否启用robots
ROBOTSTXT_OBEY = False
#对单个域名最大并发量
CONCURRENT_REQUESTS_PER_DOMAIN = 16

DOWNLOADER_MIDDLEWARES = {
    #'common.downloadermiddleware.httpproxy.RandomProxyMiddleware':100,
    'common.downloadermiddleware.useragent.RandomPCAgent': 543,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware':None,
}
#RandomProxyMiddleware 参数
#RETRY_TIMES和PROXY_USED_TIMES的比值由代理的质量决定的
HTTPPROXY_FILE_PATH = u"G:/git/proxy_scrapy/data/valid_proxy.txt"
RETRY_TIMES = 4
PROXY_USED_TIMES = 2
RETRY_HTTP_CODES = [500, 503, 504, 599, 403]
#下载超时
DOWNLOAD_TIMEOUT = 6

ITEM_PIPELINES = {
    'proxyip.pipelines.JsonWithEncodingPipeline': 800,
}
