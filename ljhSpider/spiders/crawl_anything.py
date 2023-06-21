import json

import scrapy
from scrapy_redis.spiders import RedisSpider
from ljhSpider.auto_parse import ParseNews


class CrawlAnythingSpider(RedisSpider):
    name = "crawl_anything"

    def __init__(self, redis_key=None, *a, **kw):
        super().__init__(*a, **kw)
        self.redis_key = redis_key

    def parse(self, response):
        print(response.url)
        # print(response.text)
        page_info = json.dumps(
            ParseNews().parse(response.text), ensure_ascii=False, indent=4
        )
        print(page_info)
