import pandas as pd
import pymysql
import numpy as np
from snownlp import SnowNLP
from sqlalchemy import create_engine
from mysql import connector

#链接数据库取原始产品和客户评论信息表
sql = 'SELECT * FROM shampoo'
conn = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='test123', db='usagebase', charset='utf8')
raw_data = pd.read_sql(sql, conn)

#空值判断和预处理，一旦出现空值直接删除
nonChecking = raw_data.isnull().sum()

for i in range(len(nonChecking)):
    if nonChecking[i] > 0:
        raw_data.dropna()

#去除重复记录
raw_data.drop_duplicates()

#情感分析

def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

raw_data['sentiment'] = raw_data.product_comment.apply(_sentiment)
print(raw_data)

#写入mysql
engine = create_engine('mysql+mysqlconnector://root:test123@localhost:3306/usagebase', encoding='utf8')
pd.io.sql.to_sql(raw_data, 'shampoo_senti', con = engine, index=False, if_exists='append')