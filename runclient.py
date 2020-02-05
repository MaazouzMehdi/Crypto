#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import time
import notif
import cryptocurrency


def contact_serveur(crypto) :
	r = requests.get("https://coinmarketcap.com/fr/currencies/"+crypto+"/")
	return r.text

def get_change_conversion() :
	r = requests.get("https://www.google.com/search?client=ubuntu&channel=fs&q=conversion+dollar+euro&ie=utf-8&oe=utf-8")
	i = r.text.find("class=\"BNeawe iBp4i AP7Wnd\"")
	j = r.text.find("Euro</div></div></div></div></div><div><div><div class")
	
	return(float(r.text[i+66:j-1]))

def fetch_price(start,end,response) :
	i = response.find(start)
	j = response.find(end)
	#print(response[i+8:j-2])
	return float(response[i+8:j-2])

def convert(price_usd) :
	price_eur = price_usd * get_change_conversion()
	return float(price_eur)

def percentage(old_price, new_price) :
	return ((new_price / old_price) * 100. - 100)
	
def run(cryptos) :
	for crypto in cryptos :
		response = contact_serveur(crypto.get_name())
		price_usd = fetch_price("\"price\"","priceCurrency",response)
		crypto.set_new_price(convert(price_usd))
		if crypto.get_old_price() == 0 :
			percent = 0.
		else :
			percent = percentage(crypto.get_old_price(), crypto.get_new_price())
		crypto.set_old_price(crypto.get_new_price())
		#print(crypto.new_price)
		#print(str(percent)[0:4])
		notif.show(crypto.get_name().upper(),float(str(crypto.get_new_price())[0:5]),str(percent)[0:4])

if __name__ == '__main__' :
	notif.init()
	cryptos = []
	
	cryptos.append(cryptocurrency.Cryptocurrency("xrp",0,0))
	cryptos.append(cryptocurrency.Cryptocurrency("litecoin",0,0))

	while True :
		run(cryptos)
		time.sleep(1400)
