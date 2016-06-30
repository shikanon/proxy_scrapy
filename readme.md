# proxy_scrapy
-------------------

proxy_scrapy是一个scrapy搭建的代理模块，主要包括代理抓取、代理测试和使用代理三个模块。


### 依赖包
---------------------
基于python2所写，依赖scrapy。


### 代理抓取
-------------------------
主要通过抓取一些代理网站(如：xicidaili.com等)抓获代理，启动命令。
> scrapy crawl fetch_proxyip

抓取数据生成一个ip_proxy_utf8.json文件。文件格式为`{"connect_type": "HTTP", "ip": "39.65.153.229", "port": "8888"}`


### 代理测试
-------------------------
代理ip测试，主要用于测试ip是否可以正常访问，代理测试模块为test_proxy_ip.py，输出文件为valid_proxy.txt。


### scrapy代理设置
-------------------------
scrapy代理设置，将测试通过的代理ip文件导入scrapy中，通过随机选取的方式抓取目标网站。
使用方法：
在settings下设置如下：
> DOWNLOADER_MIDDLEWARES = {'common.downloadermiddleware.httpproxy.RandomProxyMiddleware':100}
> HTTPPROXY_FILE_PATH = u"/content/proxyip/data/valid_proxy.txt"
> RETRY_TIMES = 6
> PROXY_USED_TIMES = 2
> RETRY_HTTP_CODES = [500, 503, 504, 599, 403]

`HTTPPROXY_FILE_PATH`为ip代理文件路径，`RETRY_TIMES`为请求连接失败重试次数，`PROXY_USED_TIMES` proxy失败重试次数，`RETRY_HTTP_CODES`为重试返回码。`HTTPPROXY_FILE_PATH`为必填值。
运行`python scrapy_test_api.py`测试抓取百度百科。
