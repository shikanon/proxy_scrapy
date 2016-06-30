#coding:utf8
import scrapy
from proxyip.items import IPProxyItem
from scrapy import log

class ProxyIPSpider(scrapy.Spider):
    name = "fetch_proxyip"
    allowed_domains = ["xicidaili.com"]
    start_urls = ["http://www.xicidaili.com/nt/%s"%str(i) for i in range(1,150)]

    def parse(self, response):
        log.msg(u"%s:  抓取成功!"%(response.url), level=log.INFO)
        ip_proxy = IPProxyItem()
        ip = response.xpath(".//*[@id='ip_list']/tr/td[2]/text()").extract()
        port = response.xpath(".//*[@id='ip_list']/tr/td[3]/text()").extract()
        connect_type = response.xpath(".//*[@id='ip_list']/tr/td[6]/text()").extract()
        for line in zip(connect_type, ip, port):
            ip_proxy["connect_type"], ip_proxy["ip"], ip_proxy["port"] = line
            yield ip_proxy
        #for url in response.css(".pagination>a::attr(href)").extract():
        #    yield scrapy.Request(response.urljoin(url), callback=self.parse)

    def test(self, response):
        from scrapy.shell import inspect_response
        inspect_response(response, self)
