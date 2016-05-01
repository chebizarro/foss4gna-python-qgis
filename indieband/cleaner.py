#!/usr/bin/python

import csv

def cleanfile():
	with open('venues_manual.csv','rb') as csvfile:
		filereader = csv.DictReader(csvfile)
		with open('venues_cleaned.csv','wb') as savefile:
			writer = csv.DictWriter(savefile, fieldnames=filereader.fieldnames)
			writer.writeheader()
			rows = 0
			for row in filereader:
				row['address'] = cleanrow(row)
				writer.writerow(row)	
				rows += 1		
				print row['address']
			print "Number of rows:", rows

def cleanrow(row):
	address = row['address']
	idx = address.rfind('OR')
	if idx > 0:
		address = address[0:idx+2]
	address = address.replace(' n ',' N ')
	address = address.replace(' s ',' S ')
	address = address.replace(' Se ',' SE ')
	address = address.replace(' Sw ',' SW ')
	address = address.replace(' Ne ',' NE ')
	address = address.replace(' Nw ',' NW ')
	address = address.replace(' Portland',', Portland')
	address += ', USA'
	
	return address
	
	
if __name__ == '__main__':
	cleanfile()