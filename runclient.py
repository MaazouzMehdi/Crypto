#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import time
import notif
import cryptocurrency


def contact_serveur(crypto) :
	"""
		send a request to the site coinmarketcap
		return the response that contains an HTML file with the current value of
		the cryptocurrency
	"""
	r = requests.get("https://coinmarketcap.com/fr/currencies/"+crypto+"/")
	return r.text

def get_change_conversion() :
	"""
	send a request in order to get the current exchange rate
	between the USD/EUR
	"""
	while True :
		try :
			r = requests.get("https://www.google.com/search?client=ubuntu&channel=fs&q=conversion+dollar+euro&ie=utf-8&oe=utf-8")
			i = r.text.find("EUR/USD Amerikaanse Dollar")
			return(float(r.text[i+28:i+33].replace(',','.')))
		except ValueError :
			time.sleep(60)

def fetch_price(start,end,response) :
	"""
	fetch the current value of the cryptocurrency
	in an HTML file
	"""
	i = response.find(start)
	j = response.find(end)
	return float(response[i+8:j-2])

def convert(price_usd) :
	"""
	convert a price from USD to EUR
	"""
	price_eur = price_usd / get_change_conversion()
	return float(price_eur)

def percentage(old_price, new_price) :
	"""
	compute a percentage of increasing or decreasing
	between two values
	"""
	return ((new_price / old_price) * 100. - 100)


def run(cryptos) :
	"""
	main method that call the others in order to show
	on screen an notification that contains the name of
	the cryptocurrency, it's value an the percentage of
	increasing or decreasing.
	"""
	for crypto in cryptos :
		request_ok = False
		"""
		Sometimes fetch_price raise an ValueError because he matches
		more than the price of the cryptocurrency
		"""
		while not (request_ok) :
			try:
				response = contact_serveur(crypto.get_name())
				price_usd = fetch_price("\"price\"","priceCurrency",response)
				request_ok = True
			except ValueError:
				time.sleep(60)
		crypto.set_new_price(convert(price_usd))
		if crypto.get_old_price() == 0 :
			percent = 0.
		else :
			percent = percentage(crypto.get_old_price(), crypto.get_new_price())
		crypto.set_old_price(crypto.get_new_price())
		notif.show(crypto.get_name().upper(),float(str(crypto.get_new_price())[0:5]),str(percent)[0:4])

if __name__ == '__main__' :
	notif.init()
	cryptos = []
	
	cryptos.append(cryptocurrency.Cryptocurrency("xrp",0,0))
	cryptos.append(cryptocurrency.Cryptocurrency("litecoin",0,0))

	while True :
		run(cryptos)
		time.sleep(1400)
