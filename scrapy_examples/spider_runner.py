import re
from os.path import isfile

from scrapy.cmdline import execute


def run(spider=None, output_json='test.json'):
    """
    Python equivalent to running 'scrapy runspider -o example.json spider.py' in a shell
    Use to run spiders from Celery tasks, etc.

    :param spider: spider location -- 'spider_directory/spider.py'
    :param output_json: output file -- 'json_directory/example.json'
    """

    json_regex = re.compile('(\S+).json$')

    if not isfile(spider):
        raise NotADirectoryError("A spider script location must be provided")

    if not json_regex.fullmatch(output_json):
        raise ValueError("Output file must be a JSON")

    argv = ['/usr/local/bin/scrapy', 'runspider', '-o', output_json, spider]
    execute(argv=argv)
