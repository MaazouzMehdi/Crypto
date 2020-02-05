#!/usr/bin/python
# -*- coding: utf-8 -*-

# notify2 is an API
import notify2

def init() :
	"""
	initialize a notification
	"""
	notify2.init('app name')
	

def show(crypto, value, percent) :
	"""
	show an notification at the user's screen,
	this notification includes the name of the crypto, it's value
	and the percent of increasing or decreasing
	"""
	#Initialise the D-Bus connection. Must be called before you send any notifications
	notify2.init('app name')
	
	notif = notify2.Notification(crypto + ' : '+ str(value) + ' ( '+str(percent)+ ')')
	notif.set_urgency(notify2.URGENCY_CRITICAL)
	notif.show()


