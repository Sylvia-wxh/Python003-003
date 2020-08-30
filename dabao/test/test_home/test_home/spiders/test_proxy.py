import scrapy


class TestProxySpider(scrapy.Spider):
    name = 'test_proxy'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']
    
    def parse(self, response):
        print(response.text)