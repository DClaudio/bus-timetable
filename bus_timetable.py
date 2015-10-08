from urllib2 import Request, urlopen, URLError
#import pyupm_i2clcd as lcd

from TflArrivalsResponseParser import *
from TflApiUrlBuilder import *

def requestDataFromTfl(*args):
	responseParser = TflArrivalsResponseParser() 
	request = Request(TflApiUrlBuilder().build_commondale_url())
	try:
		response = urlopen(request)
		arrivals_data = response.read()
		formated_data = responseParser.get_formated_response(arrivals_data)
		print_arrivals_console(formated_data)
	except URLError, e:
		print 'Request Error: ', e

def print_arrivals_console(data):
	print '  Bus  Time   Destination'
	for i in data:
		print '  {0:>{w0}}  {1:>{w1}}  {2:<{w2}}'.format(i['route'], i['timeToStation'], 
			i['destination'], w0=3, w1=5, w2=17)



requestDataFromTfl()




#how to use lcd
def print_on_lcd(*args):	
	# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS) 
	myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
	# RGB Red
	myLcd.setColor(255, 0, 0)
	#write on first line
	myLcd.setCursor(0,0)
	myLcd.write('Hello World')
	#write on second line
	myLcd.setCursor(1,0)
	myLcd.write('Hello World')