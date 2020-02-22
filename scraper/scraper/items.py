# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import os
import django
import scrapy

from scrapy_djangoitem import DjangoItem

from tables.models import Table


class TableItem(DjangoItem):
    django_model = Table
