#coding:utf8
# author: shikanon
import scrapy
from proxyip.items import IPProxyItem
import logging


logger = logging.getLogger(__name__)

class ProxyIPSpider(scrapy.Spider):
    name = "fetch_proxyip"
    allowed_domains = ["xicidaili.com"]
    start_urls = ["http://www.xicidaili.com/nt/%s"%str(i) for i in range(1,50)]

    def parse(self, response):
        logger.info(u"%s:  抓取成功!"%(response.url))
        ip_proxy = IPProxyItem()
        if "xpath" not in dir(response):
            yield scrapy.Request(response.url, dont_filter=True, callback=self.parse)
        ip = response.xpath(".//*[@id='ip_list']/tr/td[2]/text()").extract()
        port = response.xpath(".//*[@id='ip_list']/tr/td[3]/text()").extract()
        connect_type = response.xpath(".//*[@id='ip_list']/tr/td[6]/text()").extract()
        for line in zip(connect_type, ip, port):
            ip_proxy["connect_type"], ip_proxy["ip"], ip_proxy["port"] = line
            yield ip_proxy
        for url in response.css(".pagination>a::attr(href)").extract():
            yield scrapy.Request(response.urljoin(url), callback=self.parse)

    def test(self, response):
        from scrapy.shell import inspect_response
        inspect_response(response, self)
