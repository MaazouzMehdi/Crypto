class Cryptocurrency: #Definition of a cryptocurrency
	
	""" Include the name of the cryptocurrency, and two
		prices at different time in order to compare the percentage
		between them"""

	def __init__(self,name, old_price, __new_price) :
		self.__name = name
		self.__old_price = 0
		self.__new_price = 0
	
	def set_new_price(self,new) :
		self.__new_price = new
	
	def set_old_price(self,new) :
		self.__old_price = new

	def get_old_price(self) :
		return self.__old_price

	def get_new_price(self):
		return self.__new_price

	def get_name(self):
		return self.__name
