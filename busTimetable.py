from urllib2 import Request, urlopen, URLError
import mraa

def httpReqestExample(*args):
	request = Request('http://placekitten.com/')
	try:
		response = urlopen(request)
		kittens = response.read()
		print kittens[559:1000]
	except URLError, e:
    print 'No kittez. Got an error code:', e

def control_lcd(*args):
	x = mraa.Gpio(13)
	x.dir(mraa.DIR_OUT)
	x.write(1)