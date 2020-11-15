# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import pretty_errors


class UsagecollectPipeline:
    # def process_item(self, item, spider):
    #     return item
    
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='test123', db='usagebase')
    
    def process_item(self, item, spider):
        date = item['date']
        product_name = item['product_name']
        product_comment = item['product_comment']

        for i in range(len(product_comment)):

            try:
                cur=self.conn.cursor()
                insert_sql = """
                insert into shampoo(date, product_name, product_comment) VALUES(%s, %s, %s)
                """

                cur.execute(insert_sql, (date, product_name, product_comment[i]))
                self.conn.commit()
            except:
                self.conn.rollback()
            finally:
                cur.close()
        return item
    
    def close_conn(self):
        self.conn.close()