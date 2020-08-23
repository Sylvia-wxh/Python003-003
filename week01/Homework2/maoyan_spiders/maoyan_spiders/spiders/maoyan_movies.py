import scrapy
from scrapy.selector import Selector
from maoyan_spiders.items import MaoyanSpidersItem

class MaoyanMoviesSpider(scrapy.Spider):
    name = 'maoyan_movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

#注释默认的parse函数
    # def parse(self, response):
    #     pass

# 进入猫眼主页
    def start_requests(self):
        url = "https://maoyan.com/films?showType=3"
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

#从主页的movie-hover-info开始读取需要的信息，避开翻页。
#film_type和film_time的结构比较奇怪，div[2]和div[4]下面看似一个子节点，其实有两个.只能下探取兄弟节点
    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies[:10]:
            item = MaoyanSpidersItem()
            film_name = movie.xpath('./div[1]/span[@class="name "]/text()')
            film_type = movie.xpath('./div[2]/span/following-sibling::text()')
            film_time = movie.xpath('./div[4]/span/following-sibling::text()')
            item['film_name'] = film_name.extract_first()
            item['film_type'] = film_type.extract_first().strip()
            item['film_time'] = film_time.extract_first().strip()
            yield item