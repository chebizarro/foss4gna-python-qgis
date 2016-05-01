import unittest
from indieband.spiders.venue_spider import VenueSpider

class TestVenueSpider(unittest.TestCase):
	
	def setUp(self):
		self.spider = VenueSpider()
	
	def test_parse(self):
		results = self.spider.parse(self.spider.make_requests_from_url(self.spider.start_urls[0]))
		self.assertIsNotNone(results)
		#self.assertIs(len(results),5)
	

if __name__ == '__main__':
	unittest.main()