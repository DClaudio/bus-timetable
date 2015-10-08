from urllib2 import Request, urlopen, URLError

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