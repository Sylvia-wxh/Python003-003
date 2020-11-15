# import pandas
# import requests
# from bs4 import BeautifulSoup as bs
# from fake_useragent import UserAgent
# from time import sleep
# import lxml.etree
# import scrapy
# import os
# import sys
# from scrapy.selector import Selector

# path = os.path.abspath(os.path.dirname(sys.argv[0]))
# bs_data = bs(open(path+'/product.html', encoding='utf-8'), features='html.parser')

# # product_name = bs_data.find('h1').text.strip()
# # print(product_name)

# xx = bs_data.find('div', attrs = {'id':'commentTabBlockNew'})
# print(xx)
# pr = xx.find_all('span', attrs = {'itemprop':'description'})
# alist = []
# for i in pr:
#     alist.append(i.text.strip())
# print(alist)

# # product_comment = bs_data.find('//div[@id="commentTabBlockNew"]//span[@itemprop="description"]')
# # print(type(product_comment))
# # print(product_comment)
# # alist = []
# # for tag in product_comment:
# #     alist.append(tag.text)
# # print(alist)

import datetime
d = datetime.date.today()
target = "D/%s.dd" %d
print(target)