import logging
from scrapy_examples import spider_runner

from celery import shared_task

logger = logging.getLogger('file')


@shared_task
def health_check():
    logger.info('Task Runner is healthy 🍎')


@shared_task
def run_spiders():
    logger.info('Running spiders 🕸️️')
    spider_runner.run(spider='scrapy_examples/carrefour_spider.py', output_json='test_celery_spiders.json')

