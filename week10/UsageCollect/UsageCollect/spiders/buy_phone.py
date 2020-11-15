import scrapy
from scrapy.selector import Selector
from UsageCollect.items import UsagecollectItem
from bs4 import BeautifulSoup as bs
import datetime


class BuyPhoneSpider(scrapy.Spider):
    name = 'buy_phone'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/xifahufa/h5c4s0f0t0p1/#feed-main/']

    def parse(self, response):
        url_list = response.xpath('//li[@data-position<11]/div/div[1]/a/@href').extract()
        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse2)

    def parse2(self, response):
        item = UsagecollectItem()

        date = datetime.date.today()

        soup = bs(response.text, 'html.parser')
        product_name = soup.find('h1').text.strip()

        comment_new = soup.find('div', attrs={'id':'commentTabBlockNew'})
        all_comment = comment_new.find_all('span', attrs={'itemprop':'description'})
        product_comment = []
        for i in all_comment:
            product_comment.append(i.text.strip())
        
        item['date'] = date
        item['product_name'] = product_name
        item['product_comment'] = product_comment
        yield item


    # def start_requests(self):
    #     # url = "file:///C:/Users/Swu1/GitHub%20Code/Python003-003/week10/UsageCollect/phone.html"
    #     # url = "https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/"
    #     for url in url_list:
    #         yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)
    
    # def parse(self, response):
    #     item = UsagecollectItem()
    #     product_name = Selector(response=response).xpath('//h1/text()')