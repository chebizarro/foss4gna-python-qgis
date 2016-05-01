import scrapy
import json
import csv

class RecordStoreSpider(scrapy.Spider):
	name = "recordstore"
	allowed_domains = ["recordstoreday.com"]
	start_urls = [
		"http://recordstoreday.com/Stores?state=OR"
	]
	
	def parse(self, response):
		body = response.xpath('//div[@class=""]/script/text()').extract()[0]
		start = body.find('[')
		end = body.find(']') + 1
		storestr = body[start:end].replace(',\n}','}').replace(',\n]',']')
		stores = '{"stores":' + storestr + '}'
		
		stores_parsed = json.loads(stores)
		store_data = stores_parsed['stores']
		
		storefile = open("stores.csv", "wb")

		csvwriter = csv.writer(storefile)
		
		count = 0
		
		for store in store_data:
			if count == 0:
				header = store.keys()
				csvwriter.writerow(header)
				count += 1
			csvwriter.writerow(store.values())
		
		storefile.close()
