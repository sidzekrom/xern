import numpy as np
import scipy as sp

class latlong():
	def __init__(latitude, longitude):
		assert type(latitude) is float
		assert (90.0)>=latitude>=(-90.0)
		assert type(longitude) is float
		assert (180.0)>=longitude>=(-180.0)
		self.lat = latitude
		self.long = longitude

class wifi():
	def __init__(address):
		self.location = []
		new_address = address.strip().split('.')
		for a in range(len(new_address)):
			location.append(int(new_address[a]))
		self.address = address

class scaled_factor():
	def __init__(unit_length_gmap, unit_length_grid):
		self.scale = unit_length_gmap/unit_length_grid

