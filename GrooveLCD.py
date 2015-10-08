import pyupm_i2clcd as lcd

def init_lcd(*args):
	# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS) 
	myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
	# RGB Red
	myLcd.setColor(255, 0, 0)
	return myLcd

#how to use lcd
def print_on_lcd(myLcd, line1, line2):
	myLcd.clear()
	#write on first line
	myLcd.setCursor(0,0)
	myLcd.write(line1)
	#write on second line
	myLcd.setCursor(1,0)
	myLcd.write(line2)

# LCD documentation at : http://iotdk.intel.com/docs/master/upm/python/pyupm_i2clcd.html#pyupm_i2clcd.Jhd1313m1