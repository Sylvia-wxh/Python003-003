import pandas
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from time import sleep
import lxml.etree

#伪装头部，random user agent + cookie
user_agent = UserAgent().chrome
cookie = '__mta=146119307.1597673420335.1597936594203.1597936642218.11; uuid_n_v=v1; uuid=60E1DA50E09311EA900DBD34D8258965B45ACDC2010B4B989557BD406D5D157F; mojo-uuid=aa9712850706c7e51a8894479bdf751a; _lxsdk_cuid=173fcc1b5d0c8-05591201a0b616-b7a1334-100200-173fcc1b5d0c8; _lxsdk=60E1DA50E09311EA900DBD34D8258965B45ACDC2010B4B989557BD406D5D157F; _csrf=ffd2b0f4f7176c4788b99810b3b5066039ec8522edd9e88b652305a37c33cec7; mojo-session-id={"id":"6fcfbd3bf79462d361bb1ef2872fab52","time":1597935738498}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597754709,1597847150,1597912637,1597935739; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597936698; __mta=146119307.1597673420335.1597936642218.1597936697980.12; mojo-trace-id=26; _lxsdk_s=1740c645f01-42a-862-7e5%7C%7C39'

header = {'user-agent': user_agent, 'cookie': cookie}

#读取处理猫眼主页面
maoyan = 'https://maoyan.com/films?showType=3'

main_response = requests.get(maoyan, headers=header)
bs_data = bs(main_response.text, 'html.parser')

#取child page后缀，形成链接
alist = []
for tags in bs_data.find_all('div', attrs={'class': 'channel-detail movie-item-title'}, limit=10):
    for a_tags in tags.find_all('a'):
        alist.append(a_tags.get('href'))

urls_list = ['https://maoyan.com' + i for i in iter(alist)]
# print(urls_list)

# 遍历每一个child page，取出电影名字，类型，上映时间
sleep(10)

# 封装取电影名字，类型，上映时间的部分
def child_content(myUrl):
    child_response = requests.get(myUrl, headers=header)
    selector = lxml.etree.HTML(child_response.text)
    film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
    # print(f'电影名字：{film_name}')

    film_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[@*]/text()')
    # print(f'电影类型：{film_type}')

    film_time = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
    # print(f'上映时间：{film_time}')

    return [film_name, film_type, film_time]


film_list = []
for page in urls_list:
    film_list.append(child_content(page))
    sleep(5)

# 把取到的信息存入文件
movies = pandas.DataFrame(data=film_list)
movies.to_csv('./movies.csv', encoding='gbk', index=False, header=False)

