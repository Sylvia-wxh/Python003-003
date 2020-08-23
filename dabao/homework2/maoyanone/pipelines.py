# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv


class MaoyanonePipeline():
    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        date = item['date']
        output = f'{title}\t,{link}\t,{date}\t\n'
        with open('./maoyanmovie.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
