import scrapy


from ljhSpider.api_functions import header_api, tools_api
from ljhSpider.parse import parse_detail, url_list_search
from ljhSpider.get_html_info import by_uc, by_selenium, by_drissionpage

from ljhSpider.items import LjhspiderItem
from ljhSpider.pipelines import LjhspiderPipeline


class CrawlAnythingSpider(scrapy.Spider):
    name = "crawl_anything"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://baidu.com"]

    def parse(self, response):
        pass
