# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas


class MaoyanScrapyPipeline:
    def process_item(self, item, spider):
        movie_info_list = []
        movie_info_list.append((item['movie_title'], item['movie_type'], item['movie_date']))
        movies = pandas.DataFrame(data=movie_info_list)
        movies.to_csv('./movies.csv', encoding='utf8', index=False, header=False, mode='a')
        return item
