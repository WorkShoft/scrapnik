# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ScraperPipeline(object):
    def process_item(self, item, spider):
        return item


class TablePipeline:
    def process_item(self, item, spider):
        row = item.save()
        return row


class UserAgentsPipeline:
    def process_item(self, item, spider):
        row = item.save()
        return row
