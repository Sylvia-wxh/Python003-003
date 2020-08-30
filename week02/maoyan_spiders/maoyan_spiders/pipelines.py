# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import pretty_errors

# 本地数据库的创建信息：
# CREATE TABLE `film_list`  (
#   `ID` bigint(12) NOT NULL AUTO_INCREMENT,
#   `film_name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
#   `film_type` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
#   `film_time` datetime(6) NULL DEFAULT NULL,
#   PRIMARY KEY (`ID`) USING BTREE
# ) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

# 数据库连接:

    # dbInfo = {
    #     'host': 'localhost',
    #     'port': 3306,
    #     'user': 'root',
    #     'password': 'test123',
    #     'db': 'homework'
    # }

class MaoyanSpidersPipeline:
    
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='test123', db='homework')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        film_time = item['film_time']
        
        try:
            insert_sql = """
            insert into film_list(film_name, film_type, film_time) VALUES(%s, %s, %s)
            """

            self.cur.execute(insert_sql, (film_name, film_type, film_time))
            self.conn.commit()
        except:
            self.conn.rollback()
        return item
        # output = f'|{film_name}|\t|{film_type}|\t|{film_time}|\n\n'
        # with open('./maoyan_movie.csv', 'a+', encoding= 'gbk') as article:
        #     article.write(output)
        # return item

    def close_conn(self):
        self.cursor.close()
        self.conn.close()