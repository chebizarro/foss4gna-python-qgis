#!/usr/bin/python

import csv
import json
import urllib, urllib2

def geocode_file():
	with open('venues_cleaned.csv','rb') as csvfile:
		filereader = csv.DictReader(csvfile)
		with open('venues_geocoded.csv','wb') as savefile:
			header = ['lat','lng','name','address']
			writer = csv.DictWriter(savefile, fieldnames=header)
			writer.writeheader()
			skipped = 0
			for row in filereader:
				geom = geocode(row['name'] + ', ' + row['address'])
				if geom is not None:
					row['lng'] = geom[0]
					row['lat'] = geom[1]
				else:
					row['lng'] = ''
					row['lat'] = ''
					skipped += 1
				print row
				writer.writerow(row)
			print 'Number of skipped addresses:', skipped

def geocode(address):
	location = urllib.quote_plus(address)
	url = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % location
	response = urllib2.urlopen(url).read()
	result = json.loads(response)
	if result['status'] == 'OK':
		return (result['results'][0]['geometry']['location']['lng'],
			result['results'][0]['geometry']['location']['lat'])

	
if __name__ == '__main__':
	geocode_file()