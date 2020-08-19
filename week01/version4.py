import requests
from bs4 import BeautifulSoup as bs
import lxml.etree


myUrl = 'https://maoyan.com/films?showType=3'

user_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'

header = {}
header['user-agent'] = user_Agent

pageContent = requests.get(myUrl, headers = header)

selector = lxml.etree.HTML(pageContent.text)

film_name = selector.xpath('/html/body/div[4]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[1]/span[1]/text()')
print(f'电影名称：{film_name}')