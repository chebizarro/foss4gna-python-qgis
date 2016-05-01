import scrapy
import json
import csv
import urllib, urllib2


from indieband.items import VenueItem

class VenueSpider(scrapy.Spider):
	name = "venues"
	allowed_domains = ["pc-pdx.com"]
	start_urls = [
		"http://pc-pdx.com/venues"
	]
	
	def parse(self, response):
		for row in response.xpath('//div[@id="venue-listings"]/div'):
			venue = VenueItem()
			venue['name'] = row.xpath('div/ul/li[1]/a/text()').extract()[0].strip()
			venue['address'] = row.xpath('div/ul/li[2]/text()').extract()[0].strip()
			venue['address'] = " ".join(venue['address'].split())
			geom = self.geocode(venue['address'])
			if geom is not None:
				venue['lng'] = geom[0]		
				venue['lat'] = geom[1]		
			yield venue

	def geocode(self, address):
		location = urllib.quote_plus(address.encode('utf-8'))
		url = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % location
		response = urllib2.urlopen(url).read()
		result = json.loads(response)
		if result['status'] == 'OK':
			return (result['results'][0]['geometry']['location']['lng'],
				result['results'][0]['geometry']['location']['lat'])
