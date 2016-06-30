#coding:utf8
# author: shikanon
import tornado.httpclient
import tornado.ioloop
import json

def handle_request(response):
    if response.error:
        print "Error:", response.error
    else:
        print(response.code,response.request.proxy_host,response.request.proxy_port)
        with open("valid_proxy.txt","a") as f:
            line = "http://" + response.request.proxy_host + ":" + str(response.request.proxy_port)
            f.write(line+"\n")

def test_proxy(proxy_files):
    tornado.httpclient.AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
    http_client = tornado.httpclient.AsyncHTTPClient()
    with open(proxy_files, "r") as f:
        for line in f:
            if line:
                data = json.loads(line)
                if data["connect_type"] == "HTTP":
                    proxy_host = data["ip"]
                    proxy_port = int(data["port"])
                    request = tornado.httpclient.HTTPRequest(url="http://shikanon.com/", proxy_host=proxy_host, proxy_port=proxy_port,
                                                             connect_timeout=4)
                    http_client.fetch(request, callback=handle_request)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    test_proxy("ip_proxy_utf8.json")
