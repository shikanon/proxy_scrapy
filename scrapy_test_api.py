#coding:utf8
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy import log
import re
import string


class BaikeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    category = scrapy.Field()
    abstract = scrapy.Field()
    content = scrapy.Field()
    relevant = scrapy.Field()
    label = scrapy.Field()


class BaiduSpider(scrapy.Spider):
    name = "baidu_baike"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "http://baike.baidu.com/dili"
    ]

    def parse(self, response):
        index_urls = response.css(".g-row>span>a::attr(href)").extract() + response.css(".g-row.more-category>ul>li>h4>a::attr(href)").extract()
        for url in index_urls:
            yield scrapy.Request(response.urljoin(url), self.index_page)

    def index_page(self, response):
        #栏目页，导向同类型网页
        index_urls = response.css("#pageIndex > a::attr(href)").extract() + response.xpath(".//*[@id='content-main']/div[3]/div[2]/div[1]/div[2]/div/a/@href").extract()
        for url in index_urls:
            yield scrapy.Request(response.urljoin(url), self.index_page)
        #导向子页面
        child_urls = response.css(".list > a::attr(href)").extract()
        label = response.css("h3.title::text").extract_first()
        for child_url in child_urls:
            #meta可以传递给子页面数据
            yield scrapy.Request(response.urljoin(child_url), meta={"label":label}, callback=self.parse_data)

    def parse_data(self, response):
        item = BaikeItem()
        item["url"] = response.url
        item["name"] = response.css(".lemmaWgt-lemmaTitle-title>h1::text").extract_first()
        item["abstract"] = self.get_all_text(response.css(".lemma-summary"))
        item["content"] = self.get_all_text(response.css(".para"))
        item["label"] = map(string.strip, response.css(".taglist::text").extract() + response.css(".taglist > a::text").extract())
        item["relevant"] = map(string.strip, response.css("a::text").extract())
        #由meta传递数据得到
        item["category"] = response.meta["label"]
        log.msg(u"[%s]词条：%s  抓取成功!"%(item["url"],item["name"]), level=log.INFO)
        yield item

    def get_all_text(self, selector):
        #re.compile("<[^>]*>")为html标签,通过sub过滤到所有html标签得到text
        text = "".join(
            re.sub(re.compile("<[^>]*>"), "", sel.extract()) for sel in selector)
        return text.strip()


#get_project_settings()是字典形式，如{'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'}
process = CrawlerProcess(get_project_settings())
print(get_project_settings())
# 'followall' is the name of one of the spiders of the project.
#需要同时跑多个爬虫只需要
#process.crawl(MySpider1)
#process.crawl(MySpider2)
process.crawl(BaiduSpider)
process.start() # the script will block here until the crawling is finished
