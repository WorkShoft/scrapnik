import cfscrape
import scrapy
from scrapy.http import Request

from scraper.scraper.items import UserAgentItem


class UserAgentsSpider(scrapy.Spider):
    name = 'useragents'
    start_urls = ['https://techblog.willshouse.com/2012/01/03/most-common-user-agents']
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

    FEED_EXPORT_ENCODING = 'utf-8'
    download_delay = 5

    custom_settings = {
        'ITEM_PIPELINES': {
            'scraper.scraper.pipelines.UserAgentsPipeline': 300,
        }
    }

    def start_requests(self):
        """
        https://stackoverflow.com/questions/33247662/how-to-bypass-cloudflare-bot-ddos-protection-in-scrapy
        """

        for url in self.start_urls:
            token, agent = cfscrape.get_tokens(url, self.user_agent)
            yield Request(url, headers={'User-Agent': agent}, cookies=token)

    def parse(self, response):
        json_data = response.css('.get-the-list ::text')[1].get()
        import json
        user_agents = json.loads(response.css('.get-the-list ::text')[1].get())
        for u in user_agents:
            u['percent'] = u['percent'].rstrip('%')
            yield UserAgentItem(**u)
