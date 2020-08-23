# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanSpidersPipeline:
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        film_time = item['film_time']
        output = f'|{film_name}|\t|{film_type}|\t|{film_time}|\n\n'
        with open('./maoyan_movie.csv', 'a+', encoding= 'gbk') as article:
            article.write(output)
        return item
