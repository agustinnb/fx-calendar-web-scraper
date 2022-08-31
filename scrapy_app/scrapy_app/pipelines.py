from pydispatch import dispatcher
from scrapy import signals

from fxcalendar.models import ScrapyItem


class ScrapyAppPipeline(object):
    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'),
        )

    def process_item(self, item, spider):
        item.save()
        return item

    def spider_closed(self, spider):
        print('SPIDER FINISHED!')