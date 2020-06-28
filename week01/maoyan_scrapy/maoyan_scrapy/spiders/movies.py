import scrapy
from maoyan_scrapy.items import MaoyanScrapyItem
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['douban.com']
    start_urls = ['http://maoyan.com/films?showType=3']

    def parse(self, response):
        # 获取电影列表
        tags = Selector(response=response).xpath(
            '//div[@class="movie-item film-channel"]')
        number = 0
        movie_info_list = []
        for tag in tags:
            movie_title = tag.xpath('.//span[contains(@class,"name")]/text()').extract_first()

            hover_texts = tag.xpath(
                './/span[@class="hover-tag"]/../text()').extract()

            movie_type = hover_texts[1].strip('\n').strip()
            movie_date = hover_texts[5].strip('\n').strip()

            item = MaoyanScrapyItem()
            item['movie_title'] = movie_title
            item['movie_type'] = movie_type
            item['movie_date'] = movie_date

            number += 1
            if number >= 10:
                break

            yield item
