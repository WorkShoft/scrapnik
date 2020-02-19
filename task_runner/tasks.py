import sys
import logging

from celery import shared_task

logger = logging.getLogger(__name__)

@shared_task
def health_check():    
    logger.info('Task Runner is healthy 🍎')
