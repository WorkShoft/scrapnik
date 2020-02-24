from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraper.scraper.spiders import carrefour_spider


class Command(BaseCommand):
    help = "Run all spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(carrefour_spider.CarrefourSpider)
        process.start()
