import scrapy

from scrapy.http import Request


class CarrefourSpider(scrapy.Spider):
    name = 'carrefourspider'
    start_urls = ['https://www.carrefour.es/mesas-mesa-de-estudio-oficina/N-10ftbh0Z1jvbjnb/c']
    download_delay = 0.5

    def __init__(self):
        self.headers={'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'}
    
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers=self.headers, cookies=False)

    def parse(self, response):
        for price in response.css('.product-card__price'):
            yield {'price': price.css('::text').get()}

        for next_page in response.css('.pagination__row > a'):
            yield response.follow(next_page, self.parse, headers=self.headers, cookies=False)
