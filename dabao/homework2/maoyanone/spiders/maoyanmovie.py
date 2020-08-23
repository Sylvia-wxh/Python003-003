import scrapy
from maoyanone.items import MaoyanoneItem
from scrapy.selector import Selector


class MaoyanmovieSpider(scrapy.Spider):
    name = 'maoyanmovie'
    allowed_domains = ['maoyan.com']
    # 起始的url
    start_urls = ['https://maoyan.com/films']

    # 筛选数据
    def start_requests(self):
        url = "file://127.0.0.1/C:/Users/Swu1/GitHub Code/Python003-003/week01/homework1/123.htm"
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        item = MaoyanoneItem()
        movies = Selector(response=response).xpath('//dd')
        for movie in movies[:10]:
            title = movie.xpath(
                './div[@class="channel-detail movie-item-title"]/@title')
            # 同级目录下所有节点
            link = movie.xpath(
                '//span[contains(text(),"类型:")]/following-sibling::node()')
            date = movie.xpath(
                '//span[contains(text(),"上映时间:")]/following-sibling::node()')
            item['title'] = title.extract_first()
            item['link'] = link.extract_first().strip()
            item['date'] = date.extract_first().strip()
            # print("电影名称："+item['title'])
            # print("电影类型："+item['link'])
            # print("上映时间："+item['date'])
            yield item
