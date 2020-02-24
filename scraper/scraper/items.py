# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem

from tables.models import Table
from task_runner.models import UserAgent


class TableItem(DjangoItem):
    django_model = Table


class UserAgentItem(DjangoItem):
    django_model = UserAgent
