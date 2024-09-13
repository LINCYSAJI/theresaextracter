import scrapy


class TheresamineSpider(scrapy.Spider):
    name = "theresamine"
    allowed_domains = ["www.mytheresa.com"]
    start_urls = ["https://www.mytheresa.com/"]

    def parse(self, response):
        pass
