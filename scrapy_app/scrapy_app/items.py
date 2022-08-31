# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from fxcalendar.models import ScrapyItem

class ScrapyAppItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = ScrapyItem	
    #id=scrapy.Field()
    #ticker = scrapy.Field()
    #symbol = scrapy.Field()
    #date = scrapy.Field()
    #title = scrapy.Field()
    #description = scrapy.Field()
    #importance = scrapy.Field()
    #previous = scrapy.Field()
    #forecast = scrapy.Field()
    #country = scrapy.Field()
    #actual = scrapy.Field()
    #allDayEvent = scrapy.Field()
    #currency = scrapy.Field()
    #reference = scrapy.Field()
    #revised = scrapy.Field()
    #economicMeaning = []
    #lastUpdate = scrapy.Field()
