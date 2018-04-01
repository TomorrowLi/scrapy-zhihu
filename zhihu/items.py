# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    headline=Field()
    avatar_url=Field()
    name=Field()
    type=Field()
    url_token=Field()
    user_type=Field()





