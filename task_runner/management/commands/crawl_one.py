from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraper.scraper.spiders import user_agents, carrefour_spider

SPIDER_DICT = {
    'useragents': user_agents.UserAgentsSpider,
    'carrefourspider': carrefour_spider.CarrefourSpider,
}


class Command(BaseCommand):
    help = "Run a spider"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        spider_name = options['spider']
        process.crawl(SPIDER_DICT[spider_name])
        process.start()

    def add_arguments(self, parser):
        parser.add_argument('spider', type=str, help='name of the spider to be run')
