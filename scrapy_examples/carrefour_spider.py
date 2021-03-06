import scrapy

from scrapy.http import Request


class CarrefourSpider(scrapy.Spider):
    name = 'carrefourspider'
    start_urls = ['https://www.carrefour.es/mesas-mesa-de-estudio-oficina/N-10ftbh0Z1jvbjnb/c']
    download_delay = 0.5
    FEED_EXPORT_ENCODING = 'utf-8'
    
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'}
        
        self.site_base_url = 'https://www.carrefour.es'
        
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers=self.headers, cookies=False)

    def parse(self, response):        
        product_card = '.product-card'
        
        for product in response.css('.product-card__detail'):       
            yield {
                'price': self.str_to_float(self.get_only_text(product.css('.product-card__prices-container ::text').get())),
                'name': self.get_only_text(product.css('.product-card__title ::text').get()),
                'url': self.site_base_url + product.css('.product-card__title > .product-card__title-link ::attr(href)').get(),
            }
            
        for next_page in response.css('.pagination__row > a'):
            yield response.follow(next_page, self.parse, headers=self.headers, cookies=False)

    def get_only_text(self, text):
        """
        Replace unwanted characters with whitespace
        and return a utf-8 string
        """
        
        unwanted_chars = ['\n', '\t', '€']
        unwanted_chars_strip = [' ']
        
        just_text = text
        
        for c in unwanted_chars:
            just_text = just_text.replace(c, '')

        for c in unwanted_chars_strip:
            just_text = just_text.strip(c)

        return just_text

    def str_to_float(self, text):
        return float(text.replace(',', '.'))
