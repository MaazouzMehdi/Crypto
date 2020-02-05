#!/usr/bin/python
# -*- coding: utf-8 -*-

import notify2


""" 
notify2 is a replacement for pynotify which can be used from different GUI toolkits 
and from programs without a GUI. 
The API is largely the same as that of pynotify, but some less important parts are left out.
"""
def init() :
	notify2.init('app name')
	

def show(crypto, value, percent) :
	
	#Initialise the D-Bus connection. Must be called before you send any notifications
	notify2.init('app name')
	
	notif = notify2.Notification(crypto + ' : '+ str(value) + ' ( '+str(percent)+ ')')
	notif.set_urgency(notify2.URGENCY_CRITICAL)
	notif.show()


