# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IndiebandItem(scrapy.Item):
	# define the fields for your item here like:
	name = scrapy.Field()
    
class VenueItem(scrapy.Item):
	name = scrapy.Field()
	address = scrapy.Field()
	lat = scrapy.Field()
	lng = scrapy.Field()