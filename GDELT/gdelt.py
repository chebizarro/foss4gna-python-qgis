#!/usr/bin/python

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry

Base = declarative_base()

class Lake(Base):
	__tablename__ = 'GDELT'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	geom = Column(Geometry('POINT'))
		

class GDELTLoader(object):

	def __init__(self):
		self.engine = create_engine('postgresql://user@localhost/user', echo=True)
		
if __name__ == '__main__':
	pass