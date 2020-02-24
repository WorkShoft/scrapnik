import logging

from celery import shared_task
from django.core.management import call_command

logger = logging.getLogger('file')


@shared_task
def health_check():
    logger.info('Task Runner is healthy 🍎')


@shared_task
def crawl():
    """
    Run crawl command defined in management/commands/crawl.py 
    """

    logger.info('Spiders are crawling 🕸️️')
    call_command('crawl')
    logger.info('Spiders just finished crawling 🕸️️')
